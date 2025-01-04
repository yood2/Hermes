from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..models.stock import Stock
from ..persist.connection import get_session

router = APIRouter()

@router.get('/{ticker}', response_model=Stock)
def get_stock(ticker: str, session: Session = Depends(get_session)):
    # Check if stock exists in database
    statement = select(Stock).where(Stock.ticker == ticker.upper())
    stock = session.exec(statement).first()
    
    # If stock doesn't exist, create it
    if stock is None:
        try:
            stock = Stock(ticker=ticker.upper())
            session.add(stock)
            session.commit()
            session.refresh(stock)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error creating stock")
    
    return stock
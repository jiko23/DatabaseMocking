from Database import Mock_Database as MDb
import datetime as dt
from fastapi import FastAPI

app = FastAPI()


def assetClassFiltering(assetClass):
    keys = []

    if(assetClass != None):
        for k, v in MDb.items():
            if(v.asset_class == assetClass):
                keys.append(k)
    return keys

def priceFiltering(maxPrice, minPrice):
    keys = []

    if((maxPrice > 0.0) and (minPrice > 0.0)):
        for k, v in MDb.items():
            if((v.trade_details.price >= minPrice) and (v.trade_details.price <= maxPrice)):
                keys.append(k)
    return keys

def tradeTypeFiltering(tradeType):
    keys = []

    if(tradeType != None):
        for k, v in MDb.items():
            if(v.trade_details.buySellIndicator == tradeType):
                keys.append(k)
    return keys

def dateFiltering(start, end):
    keys = []

    if((start != None) and (end != None)):
        start = dt.datetime.strptime(start, "%Y-%m-%d").date().isoformat()
        end = dt.datetime.strptime(end, "%Y-%m-%d").date().isoformat()
        
        for k, v in MDb.items():
            convertedDate = v.trade_date_time.date().isoformat()
            if((convertedDate >= start) and (convertedDate <= end) ):
                keys.append(k)
    return keys

@app.get("/tradelist", tags = ["Trade List"])
async def getTradeList():
    try:
        return list(MDb.values())
    except Exception as ex:
        return {"Error": ex}

@app.get("/trade/{trade_id}", tags = ["Trade by ID"])
async def getTradeByID(trade_id: str):
    try:
        return MDb[trade_id]
    except Exception as ex:
        return {"Error": "trade_id not present in DB"}

@app.get("/searchTrade/{value}", tags = ["Trade Match"])
async def searchTrade(value: str):
    try:
        temp = []
        for key, val in MDb.items():
            if(val.counterparty == value):
                temp.append(key)
            elif(val.instrument_name == value):
                temp.append(key)
            elif(val.trader == value):
                temp.append(key)
            elif(val.instrument_id == value):
                temp.append(key)
        return {"Available Trades": [MDb[key] for key in temp]}
    except Exception as ex:
        return {"Error": "Does not match"}

@app.get("/filterTrade", tags = ["Filter Trade"])
async def filterTrade(
    asset_class: str = None,
    max_price: float = 0.0,
    min_price: float = 0.0,
    trade_type: str = None,
    endDate: str = None,
    startDate: str = None
):
    try:
        if(asset_class != None):
            keys = assetClassFiltering(asset_class)
            return {"Trades": [MDb[k] for k in keys]}
        elif((max_price > 0.0) and (min_price > 0.0)):
            keys = priceFiltering(max_price, min_price)
            return {"Trades": [MDb[k] for k in keys]}
        elif(trade_type != None):
            keys = tradeTypeFiltering(trade_type)
            return {"Trades": [MDb[k] for k in keys]}
        elif((endDate != None) and (startDate != None)):
            keys = dateFiltering(startDate, endDate)
            return {"Trades": [MDb[k] for k in keys]}
    except Exception as ex:
        return {"Error": ex}
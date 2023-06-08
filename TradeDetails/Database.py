from Models import Trade, TradeDetails

Mock_Database = {
    "1": Trade(
        assetClass = "Bond",
        counterparty = "Aman Joshi",
        instrumentId = "TSLA",
        instrumentName = "Tesla INC",
        tradeDateTime = "2032-04-23T10:20:30.400+02:30",
        tradeDetails = TradeDetails(
            buySellIndicator = "SELL",
            price = 350.00,
            quantity = 10000
        ),
        tradeId = "1",
        trader = "Aman Sulh",
    ),

    "2": Trade(
        assetClass = "Bond",
        counterparty = "Aman Soni",
        instrumentId = "AMZ",
        instrumentName = "Amazon INC",
        tradeDateTime = "2032-04-22T10:20:30.400+02:30",
        tradeDetails = TradeDetails(
            buySellIndicator = "SELL",
            price = 200.00,
            quantity = 12000
        ),
        tradeId = "2",
        trader = "Billas Kohli",
    ),

    "3": Trade(
        assetClass = "Equity",
        counterparty = "Aman Soni",
        instrumentId = "AMZ",
        instrumentName = "Amazon INC",
        tradeDateTime = "2032-08-24T10:20:30.400+02:30",
        tradeDetails = TradeDetails(
            buySellIndicator = "BUY",
            price = 100.00,
            quantity = 22000
        ),
        tradeId = "3",
        trader = "Aman Sulh",
    )
}


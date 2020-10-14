notifications_by_user_id_query = """
    query UserNotifications($userId: ID!) {
       notificationsByUserId(userId: $userId) {
          id   
          message
          read
          notificationTimestamp
       }
    }
    """

user_by_auth_token_query = """
    query GetUserByAuthToken($authToken: String!) {
      userByAuthToken(authToken: $authToken) {
        id
        firstName
        lastName
        authToken
        userStocks {
          id
          stock {
            id
            name
            symbol
          }
        }
      }
    }
    """

user_by_username_query = """
    query GetUserByUsername($username: String!) {
      userByUsername(username: $username) {
        id
        firstName
        lastName
        authToken
        userStocks {
          id
          stock {
            id
            name
            symbol
            currentPrice
            openPrice
            highPrice
            lowPrice
            previousClosePrice
            volume
            percentChange
            priceChange
            latestTradingDate
            latestDailyTimeSeriesEvent {
              id
              eventDate
              openPrice
              closePrice
              highPrice
              lowPrice
              volume
            }
            dailyTimeSeriesEvents(limit: 30) {
              id
              eventDate
              openPrice
              closePrice
              highPrice
              lowPrice
              volume
            }
            intradayTimeSeriesEvents(limit: 100) {
              id
              eventDatetime
              openPrice
              closePrice
              highPrice
              lowPrice
              volume
            }
          }
        }
      }
    }
    """

get_orders_by_username_query = """
    query GetUserByUsername($username: String!) {
      userByUsername(username: $username) {
        userStocks {
          id
          companyName
          stockSymbol
          orders {
            id
            priceInCents
            sharesCount
            totalAmountInCents
            orderTimestamp
            transactionType
          }
        }
      }
    }
    """

get_user_stocks_query = """
    query GetUserByUsername($username: String!) {
      userByUsername(username: $username) {
        userStocks {
          id
          companyName
          stockSymbol
        }
      }
    }
    """

get_metrics_query = """
    query RetrieveAllMetrics {
       metrics {
          id
          name
       }
    }
    """

symbol_search_query = """
    query SymbolSearch($keywords: String!) {
       symbolSearch(keywords: $keywords) {
          symbol
          name
       }
    }
    """

get_all_stocks_query = """
    query AllStocks {
       stocks {
          id
          name
          symbol
       }
    }
    """

simple_moving_average_by_stock_id_query = """
    query StockSimpleMovingAverageAnalyticByStockID($id: ID!) {
      stockById(id: $id) {
        id
        name
        symbol
        simpleMovingAverageAnalytics {
          id
          intervalType
          seriesType
          timePeriod
          simpleMovingAverageEntries {
             id
             eventTimestamp
             observationValueInCents
          }
        }
      }
    }
    """

get_stock_by_id_query = """
    query StockByID($id: ID!) {
      stockById(id: $id) {
        id
        name
        symbol
        currentPrice
        openPrice
        highPrice
        lowPrice
        previousClosePrice
        volume
        percentChange
        priceChange
        latestTradingDate
        latestDailyTimeSeriesEvent {
          id
          eventDate
          openPrice
          closePrice
          highPrice
          lowPrice
          volume
        }
        dailyTimeSeriesEvents(limit: 14) {
          id
          eventDate
          openPrice
          closePrice
          highPrice
          lowPrice
          volume
        }
        intradayTimeSeriesEvents(limit: 100) {
          id
          eventDatetime
          openPrice
          closePrice
          highPrice
          lowPrice
          volume
        }
        simpleMovingAverageAnalytics {
          id
          intervalType
          seriesType
          timePeriod
        }
      }
    }
    """
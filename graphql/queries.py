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

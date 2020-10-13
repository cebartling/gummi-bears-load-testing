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

update_user_mutation = """
    mutation UpdateUser($input: UpdateUserMutationInput!) {
       updateUser(input: $input) {
          clientMutationId 
          user {
             id
          }
       }
    }
    """

create_user_mutation = """
    mutation CreateUser($input: CreateUserMutationInput!) {
       createUser(input: $input) {
          clientMutationId 
          user {
             id
          }
       }
    }
    """

create_order_mutation = """
    mutation CreateOrder($input: CreateOrderMutationInput!) {
      createOrder(input: $input) {
        clientMutationId
        message
        errors
        order {
          id
        }
      }
    }
    """

create_stock_and_associate_with_user_mutation = """
    mutation CreateStock($input: CreateStockMutationInput!) {
       createStock(input: $input) {
          clientMutationId 
          message
          errors
          userStock {
             id
             stock {
                id
             }
          }
       }
    }
    """

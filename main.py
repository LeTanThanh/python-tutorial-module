if __name__ == "__main__":
  # Importing module objects

  import pricing
  import pricing as selling_price
  from pricing import get_net_price
  from pricing import get_net_price as calculate_net_price

  net_price = pricing.get_net_price(
    price = 100,
    tax_rate = 0.01
  )
  print(net_price)

  net_price = selling_price.get_net_price(
    price = 100,
    tax_rate = 0.01
  )
  print(net_price)

  net_price = get_net_price(
    price = 100,
    tax_rate = 0.01
  )
  print(net_price)

  net_price = calculate_net_price(
    price = 100,
    tax_rate = 0.01
  )
  print(net_price)

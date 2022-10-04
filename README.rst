.. code:: python

  import asyncio
  import logging

  from ppgee import PPGEE

  logging.basicConfig(level=logging.INFO)


  async def main() -> None:
      cpf = "00011122233"
      async with PPGEE(user=cpf, password=cpf) as ppgee:
          frequency_page = await ppgee.frequency()
          print(frequency_page.history())
          await frequency_page.confirm()
          await asyncio.sleep(5)


  if __name__ == "__main__":
      asyncio.run(main())

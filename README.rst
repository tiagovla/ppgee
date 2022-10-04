.. code:: python

  import asyncio
  from ppgee import PPGEE


  async def main():
      cpf = "00011122233"
      async with PPGEE(user=cpf, password=cpf) as ppgee:
          response = await ppgee.frequency()
          if "Opção não disponível" in response:
              print("Not ready yet")
          await asyncio.sleep(5)


  if __name__ == "__main__":
      asyncio.run(main())

import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)
from ppgee import PPGEE


async def main():
    cpf = "00011122233"
    async with PPGEE(cpf, cpf) as ppgee:
        response = await ppgee.frequency()
        if "Opção não disponível" in response:
            print("Not ready yet")
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())

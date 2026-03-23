import websockets
import json
import redis
import asyncio
from src.modules.ingestion.constants import BINANCE_BASE_URL
from src.modules.ingestion.dependencies import get_redis_client
from src.modules.ingestion import exception



async def get_binance_data():
    url = BINANCE_BASE_URL

    async with websockets.connect(url) as ws:
        async with get_redis_client() as client:

            while True:
                try:
                    raw_message = await ws.recv()
                except websockets.exception.ConnectionClosed:
                    raise exception.BinanceConnectionError

                try:
                    raw_message_dict = json.loads(raw_message)
                except json.JSONDecodeError:
                    raise exception.MessageError
            
                flat = {
    "event_type":        raw_message_dict["e"],
    "event_time":        raw_message_dict["E"],
    "symbol":            raw_message_dict["s"],
    "kline_start_time":  raw_message_dict["k"]["t"],
    "kline_close_time":  raw_message_dict["k"]["T"],
    "interval":          raw_message_dict["k"]["i"],
    "first_trade_id":    raw_message_dict["k"]["f"],
    "last_trade_id":     raw_message_dict["k"]["L"],
    "open_price":        float(raw_message_dict["k"]["o"]),
    "close_price":       float(raw_message_dict["k"]["c"]),
    "high_price":        float(raw_message_dict["k"]["h"]),
    "low_price":         float(raw_message_dict["k"]["l"]),
    "base_volume":       float(raw_message_dict["k"]["v"]),
    "trade_count":       raw_message_dict["k"]["n"],
    "is_closed":         int(raw_message_dict["k"]["x"]),
    "quote_volume":      float(raw_message_dict["k"]["q"]),
    "taker_buy_volume":  float(raw_message_dict["k"]["V"]),
    "taker_buy_quote":   float(raw_message_dict["k"]["Q"]),
}
                try:
                    await client.xadd("trade", flat)
                except:
                    raise
            


if __name__ == '__main__':
    asyncio.run(get_binance_data())


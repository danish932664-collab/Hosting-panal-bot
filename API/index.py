from main import app
from aiohttp import web

# Vercel के लिए handler
async def handler(request):
    return await app.handle_request(request)

# Vercel को handler export करें
__all__ = ['handler']

class RedisController:
    async def set_status(self, app):
        await app.redis.set('key', 'status-value')
        value = await app.redis.get('key', encoding='utf-8')
        return {"message": value}

    async def get_status(self, app, request):
        key = request.args.get('key')
        return await app.redis.get(key, encoding='utf-8')

def handler(request):
    return {
        "statusCode": 200,
        "body": '{"message": "Vercel Python API is working 🚀"}',
        "headers": {
            "Content-Type": "application/json"
        }
    }

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.urls import resolve  
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logger.info('Initialized JWTMiddleware')

    def __call__(self, request):
        current_url_name = resolve(request.path_info).url_name
        logger.info('Current URL: %s', current_url_name)

        skip_auth_urls = ['register', 'login', 'token_obtain_pair', 'token_refresh','custom_token_refresh']
        
        if current_url_name not in skip_auth_urls:
            jwt_authenticator = JWTAuthentication()
            logger.info('Inside JWT authentication in middleware')

            try:
                auth_result = jwt_authenticator.authenticate(request)
                if auth_result is not None:
                    user, token = auth_result
                    request.user = user
                else:
                    logger.warning('JWT token not provided or invalid')
                    return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=403)

            except AuthenticationFailed as e:
                logger.error('Authentication failed: %s', str(e))
                return JsonResponse({'detail': 'Invalid or expired token.'}, status=403)

            except Exception as e:
                logger.error('Unexpected error in JWT authentication: %s', str(e))
                return JsonResponse({'detail': 'Unexpected error during authentication.'}, status=500)

        response = self.get_response(request)
        return response

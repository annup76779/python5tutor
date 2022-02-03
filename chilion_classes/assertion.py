from datetime import datetime, timezone, timedelta
from calendar import timegm
from functools import wraps

def time_to_expiration(func):
		@wraps(func)
		def decorator(*args, **kwargs):
			"""Gets the expiration time fo the JWT_TOKEN"""
			expiration = get_jwt()["exp"] - timegm(datetime.now(timezone.utc).utctimetuple())
			json = func(*args, **kwargs)
			if isinstance(json, dict):
				json["exp"] = expiration
				return json
		return decorator

def get_jwt():
	s = dict(exp = timegm(
				(datetime.now(timezone.utc) + timedelta(seconds=40)).utctimetuple()
				)
			)
	print(s)
	return s

def jwt_required(func):
		@wraps(func)
		def decorator(*args, **kwargs):
			"""Gets the expiration time fo the JWT_TOKEN"""
		    # expiration = exp - timegm(datetime.now(timezone.utc))

			return func(*args, **kwargs)
		return decorator

@time_to_expiration
@jwt_required
def get_exptime():
	k = dict(status = "lsdkf")
	return k

s = get_exptime()

print(s)
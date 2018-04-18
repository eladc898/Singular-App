import urllib.request as url
import urllib.parse as parse
import json

__author__ = 'elad'

print("hello from pycharm")

opener = url.build_opener()
opener.addheaders.append(('Cookie', '_security_atlas_session=RnRwSkVBVkplbkE1ZTBqN0haV1orMW8xbnV0VFBObjRaVGd3WUhtZDdoZlBIWXhDRGdWVXV3UDdOTzVkV2d3MUxKUlUrcDg3Mm15WGNqdnJoazBLcS90Z3g0dkxsamVKeHRrY1pGVXlOd0piOGhqdFZmNDMrbG43MlRKODQ5TVB4TmdSdEFkcjNkZSsvanlnT25WeUttQzhWakRnQXRQNDFIWlNTOTJ3R2pROUJBMWxkR013TDliVVB0VDdCRGVLOVF3RW1KS0Q2UW55TS9HSWszYTJmMGpYY1dLODBveWgrbzgvOEJuNWxaNnE4cG5ETW5LYzBqQnNiR0d3NEVTTEVxNDNCRVZib2ZYQkswUXNsTE1kcXUyaHNNZVhvT1N2dWZ0b00zbUVCTlpCb2JTelg0UEJEd2hIeWlBcEFjQ3Njcy9xclZGM0pQVm1WZGlpbDBQSnZIeGJVKzJzMTJ5Z2ZYM1dKbkhRcTM2bWRYTVYwdlRlSVRZWGwwSnE2RFJaWkk0TmpEYjFjKzh4WmhaYk9XSk1jTmtQbG5DV2FxSm9jVjNFQk00a2twWEdCUVl6RXEwSVM2cCtuMWVyVGVpYlZ6SllsVFRIdHg1RThpZmo4Yk5UVFhEOVl3QmlvRk8rNWNzaXdXaHJneUplSFNRTTRNUVN1NDVFREt1WUduOHFiL00wRWUwcTk4Sk1McUxLbzRGV1Y1azBEbkdNaGoxQW9MVzVMNDA5ZG03UCt6UjlHNCtZRVFwbmp4MWcweUtELS1ySCtXTmJpa0p4bVErNjBVSkpyNVNnPT0%3D--0bb3e587c3f6a3907d6c346cd54fa3259ef57780'))

params = parse.urlencode({'station': 'DAR'})
url1 = "http://www.lvh.me:3000/station/flights?%s" % params
contents = opener.open(url1).read().decode('utf-8')
contents = json.loads(contents)
for c in contents:
    # print(c['id'])
    print('id: %d, flight_number: %s' % (c['id'], c['number']))


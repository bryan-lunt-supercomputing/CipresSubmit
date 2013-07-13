#import sys
import CipresSubmit.plugins as P

class MyDirect(P.DirectJobPlugin):
	pass

def check_appropriate(cluster_info,cmdline,submit_env,properties=dict()):
	if properties.get('is_direct',False) or cmdline.split()[0] == "this":
		return MyDirect(cluster_info,cmdline,submit_env,properties)
	return None

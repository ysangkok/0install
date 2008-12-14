# Copyright (C) 2008, Thomas Leonard
# See the README file for details, or visit http://0install.net.

from zeroinstall import support

def get_fetch_info(policy, impl):
	"""Get the text for a Fetch column."""
	if impl is None:
		return ""
	elif policy.get_cached(impl):
		if impl.id.startswith('/'):
			return '(local)'
		elif impl.id.startswith('package:'):
			return '(package)'
		else:
			return '(cached)'
	else:
		peer = policy.choose_best_peer(impl)
		if peer:
			return "(p2p)"
		src = policy.fetcher.get_best_source(impl)
		if src:
			return support.pretty_size(src.size)
		else:
			return '(unavailable)'

import dictionary

class Error(Exception):
	def __init__(self, status):
		self.status = status
		self.message = dictionary.errors_messages[status]

	def to_json(self):
		return {
			dictionary.status : self.status,
			dictionary.message : self.message	
		}

class ServerError(Error):
	def __init__(self, status):
		self.status = status
		self.message = dictionary.errors_messages[status]


class ClientError(Error):
	def __init__(self, status, message):
		self.status = status
		self.message = dictionary.errors_messages[status] + message
def __file__(filename, mode):
	try:
		f = open(filename, mode, encodings = "UTF-8")
	except IOError as e:
    	return e
	except Exception as e:
    	return e
	else:
    	return f
	finally:
		f.close()

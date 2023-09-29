import re
def clean_src_text(src_text):
	"""
	    Cleans up source text by removing HTML entities, extra whitespace, and leading/trailing whitespace.
	    Args:
	        source_text (str): The input source text to be cleaned.
	    Returns:
	        str: The cleaned source text.
	    """
	src_text = re.sub(r'(\&nbsp;)', r'', src_text, flags = re.MULTILINE)
	src_text = re.sub(r'\s+', r' ', src_text, flags = re.MULTILINE)
	return clean_text.strip()


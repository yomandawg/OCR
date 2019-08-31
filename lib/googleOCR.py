# GOOGLE TEXT OCR API

def detect_text(path):
	import io
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()

	with io.open(path, 'rb') as image_file: content = image_file.read()

	image = vision.types.Image(content=content)

	response = client.text_detection(image=image)
	texts = response.text_annotations

	# print('Texts:')
	
	temp = []

	for text in texts:
		temp.append(text.description)

		# print('\n"{}"'.format(text.description))

		# vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])

		# print('bounds: {}'.format(','.join(vertices)))

	return temp


def detect_document(path):
	import io
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()

	with io.open(path, 'rb') as image_file:
		content = image_file.read()

	image = vision.types.Image(content=content)

	response = client.document_text_detection(image=image)

	temp = []

	for page in response.full_text_annotation.pages:
		for block in page.blocks:
			# print('\nBlock confidence: {}\n'.format(block.confidence))

			for paragraph in block.paragraphs:
				# print('Paragraph confidence: {}'.format(paragraph.confidence))

				for word in paragraph.words:
					word_text = ''.join([
						symbol.text for symbol in word.symbols
					])
					# print('Word text: {} (confidence: {})'.format(word_text, word.confidence))

					temp.append((word_text, word.confidence))

					# for symbol in word.symbols:
					# 	print('\tSymbol: {} (confidence: {})'.format(
					# 		symbol.text, symbol.confidence))
	
	return temp
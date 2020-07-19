import math
import xml.etree.ElementTree as etree

class DataPuller:
	"""
	Data Puller
	"""
	def __init__(self):
		pass

	def createSpawnPointDatas(self):
		"""
		"""
		res = "C:/Users/Black/Ouroboros/prototyping/novice_1_spawn_points.xml"

		tree = etree.parse(res)
		root = tree.getroot()

		for child in root:
			positionNode = child[0][0][0]
			directionNode = child[0][0][1]
			scaleNode = child[0][0][2]

			scaleMod = int(((float(scaleNode[0].text) + float(scaleNode[1].text) + float(scaleNode[2].text)) / 3.0) * 10)
			scale = (float(scaleNode[0].text), float(scaleNode[1].text), float(scaleNode[2].text))
			position = (float(positionNode[0].text), float(positionNode[1].text), float(positionNode[2].text))
			direction = [float(directionNode[0].text) / 360 * (math.pi * 2),
						 float(directionNode[1].text) / 360 * (math.pi * 2),
						 float(directionNode[2].text) / 360 * (math.pi * 2)]

			if direction[0] - math.pi > 0.0:
				direction[0] -= math.pi * 2
			if direction[1] - math.pi > 0.0:
				direction[1] -= math.pi * 2
			if direction[2] - math.pi > 0.0:
				direction[2] -= math.pi * 2

			#print([int(child.attrib['name'])])
			print(child[0].attrib['Name'])
			print(scale)
			print(position)
			print(direction)
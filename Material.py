class Material (object):
  #difuse se refiere al color de la superficie. Que cuando una superficie esta iluminaada de cierto luz que color refleja
  def __init__(self, difuse, spec = 1.0 , ks = 0.0):
    self.diffuse = difuse
    self.spec = spec
    self.ks = ks
  def GetSurfaceColor(self, intercept, renderer):

    lightColor = [0,0,0]
    finalColor = self.diffuse
    for light in renderer.lights:
      shadowIntercept = None
      if light.lightType == "Directional":
        lightDir = [-x for x in light.direction]
        shadowIntercept = renderer.glCastRay(intercept.point, lightDir, intercept.obj)
      
      if shadowIntercept == None:
        currectLightCOlor = light.GetLightColor(intercept)
        currentSpecularCOlor = light.GetSpecularColor(intercept, renderer.camera.translate)
        lightColor = [(lightColor[i] + currectLightCOlor[i] + currentSpecularCOlor[i]) for i in range (3)]

    finalColor = [(finalColor[i] * lightColor[i]) for i in range(3)]
    finalColor = [min(1, finalColor[i]) for i in range(3)]
    return finalColor
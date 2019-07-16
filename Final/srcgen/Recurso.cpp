class Recurso:

  def __init__(this):
      estado = Estado()
      categoria = Categoria()
      historial = Historial()

  def __init__(this,codigo,nombre,descripcion):
      this.codigo=codigo
      this.nombre=nombre
      this.descripcion=descripcion
      estado = Estado()
      categoria = Categoria()
      historial = Historial()

  def getCodigo():
    return this.codigo

  def getNombre():
    return this.nombre

  def getDescripcion():
    return this.descripcion

  def getEstado():
    return this.estado

  def getCategoria():
    return this.categoria

  def getHistorial():
    return this.historial

  def setCodigo(this,codigo):
    this.codigo = codigo

  def setNombre(this,nombre):
    this.nombre = nombre

  def setDescripcion(this,descripcion):
    this.descripcion = descripcion

  def setEstado(this,estado):
    this.estado = estado

  def setCategoria(this,categoria):
    this.categoria = categoria

  def setHistorial(this,historial):
    this.historial = historial


class Cuenta:

  def __init__(this):
      estado = Estado()
      historial = Historial()

  def __init__(this,codigo,nombre,apellido,mail,telefono):
      this.codigo=codigo
      this.nombre=nombre
      this.apellido=apellido
      this.mail=mail
      this.telefono=telefono
      estado = Estado()
      historial = Historial()

  def getCodigo():
    return this.codigo

  def getNombre():
    return this.nombre

  def getApellido():
    return this.apellido

  def getMail():
    return this.mail

  def getTelefono():
    return this.telefono

  def getEstado():
    return this.estado

  def getHistorial():
    return this.historial

  def setCodigo(this,codigo):
    this.codigo = codigo

  def setNombre(this,nombre):
    this.nombre = nombre

  def setApellido(this,apellido):
    this.apellido = apellido

  def setMail(this,mail):
    this.mail = mail

  def setTelefono(this,telefono):
    this.telefono = telefono

  def setEstado(this,estado):
    this.estado = estado

  def setHistorial(this,historial):
    this.historial = historial


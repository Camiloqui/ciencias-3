class Prestamo:

  def __init__(this):
      recurso = Recurso()
      cuenta = Cuenta()
      estado = Estado()

  def __init__(this,codigo,fechaIn,fechaFin,fechaOut,observacion):
      this.codigo=codigo
      this.fechaIn=fechaIn
      this.fechaFin=fechaFin
      this.fechaOut=fechaOut
      this.observacion=observacion
      recurso = Recurso()
      cuenta = Cuenta()
      estado = Estado()

  def getCodigo():
    return this.codigo

  def getFechain():
    return this.fechaIn

  def getFechafin():
    return this.fechaFin

  def getFechaout():
    return this.fechaOut

  def getObservacion():
    return this.observacion

  def getRecurso():
    return this.recurso

  def getCuenta():
    return this.cuenta

  def getEstado():
    return this.estado

  def setCodigo(this,codigo):
    this.codigo = codigo

  def setFechain(this,fechaIn):
    this.fechaIn = fechaIn

  def setFechafin(this,fechaFin):
    this.fechaFin = fechaFin

  def setFechaout(this,fechaOut):
    this.fechaOut = fechaOut

  def setObservacion(this,observacion):
    this.observacion = observacion

  def setRecurso(this,recurso):
    this.recurso = recurso

  def setCuenta(this,cuenta):
    this.cuenta = cuenta

  def setEstado(this,estado):
    this.estado = estado


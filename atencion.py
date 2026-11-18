class Atencion:
    def __init__(self, codigo, cita, motivo):
        self._codigo = codigo
        self._cita = cita
        self._motivo = motivo

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def cita(self):
        return self._cita

    @property
    def motivo(self):
        return self._motivo

    # Setters
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @cita.setter
    def cita(self, valor):
        self._cita = valor

    @motivo.setter
    def motivo(self, valor):
        self._motivo = valor

    def resumen(self):
        return (f"{self._codigo}-{self._cita.paciente.nombre} atendido por el Dr. "
                f"{self._cita.medico.nombre}. Motivo: {self._motivo}")

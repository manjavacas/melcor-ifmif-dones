
# DUDAS MANUEL V.

1. ¿El hourly leak rate con cuánto tiempo lo calculamos? Porque una vez que llegue al estado de equilibrio, cuanto más tiempo pase menor será, así que yo cogería el mismo tiempo (1h) que para medir la presión y la temperatura según el ISO 10648-2 'Pressure change method'.
      
> ANTONIO: intenta utilizar el mismo tiempo que utilicé en los cálculos para la fuga C002 - R016. Son 1.0e+05 seg. Tienes todo el proceso en el informe `calculo_fugas.pdf`, donde se detalla como aplicar el Oxygen Method.
> MANUEL V.: lo he estado mirando, pero para la R110 habría que aplicar otro método (el del changing pressure) ya que no hay gases inertes dentro sino aire. Lo que pasa para el hourly rate es que, cuando pasan por ejemplo 1.0E+04 seg, el sistema se me estabiliza y aunque pase el tiempo, la presión final no va a variar y el Tf va a disminuir inevitablemente, lo que me hace pensar que el tiempo no debe ser arbitrario porque entonces validar una fuga es cuestión de dejarla suficiente tiempo... Si miras el anexo B del ISO 10648-2, ves que para el Tf coge t=60 min, que es el tiempo de medida que establecen antes para la variación de presión y temperatura. Además, la prsión incial debe bajarse 1000 Pa por lo que he leído, no sé por qué usáis 40 Pa.

2. Para una habitación fija, ¿los cálculos de fugas se consideran para todas en conjunto (una por habitación con la que se conecta) o cada fuga individual?. Supongo que el hourly leak rate es para toda la habitación y habría que sumar las contribuciones de cada fuga o para cada fuga va por separado.
En concreto, me ocurre que la R110 tiene una diferencia entre aire que entra y que sale por el HVAC de unos 2000 m3/h, lo que hace que en una fuga de 1.75 cm2 (lo máximo que me ha dejado el ISO) tenga que llevar el aire velocidades ultrasónicas xd. Si se pudieran poner fugas por cada conexión, a lo mejor sí es posible.

3. ¿Podríais subir aquí el código original de EAI?

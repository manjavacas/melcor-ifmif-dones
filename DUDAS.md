
# DUDAS MANUEL V.

1. ¿El hourly leak rate con cuánto tiempo lo calculamos? Porque una vez que llegue al estado de equilibrio, cuanto más tiempo pase menor será, así que yo cogería el mismo tiempo (1h) que para medir la presión y la temperatura según el ISO 10648-2 'Pressure change method'.
      
> ANTONIO: intenta utilizar el mismo tiempo que utilicé en los cálculos para la fuga C002 - R016. Son 1.0e+05 seg. Tienes todo el proceso en el informe `calculo_fugas.pdf`, donde se detalla como aplicar el Oxygen Method.

> MANUEL V.: lo he estado mirando, pero para la R110 habría que aplicar otro método (el del changing/constant pressure) ya que no hay gases inertes dentro sino aire. Lo que pasa para el hourly rate es que, cuando pasan por ejemplo 1.0E+04 seg, el sistema se me estabiliza y aunque pase el tiempo, la presión final no va a variar y el Tf va a disminuir inevitablemente, lo que me hace pensar que el tiempo no debe ser arbitrario porque entonces validar una fuga es cuestión de dejarla suficiente tiempo... Si miras el anexo B del ISO 10648-2, ves que para el Tf coge t=60 min, que es el tiempo de medida que establecen antes para la variación de presión y temperatura (que por cierto, se deben igualar las temperaturas antes de hacer la prueba?). Además, la presión incial debe bajarse 1000 Pa por lo que he leído, no sé por qué usáis 40 Pa.

> ANTONIO: lo vemos en la próxima reunión. Algunos apuntes (sobre el Oxygen Method, que es el que yo apliqué en la LLC):
> * ¿A qué te refieres con que "el TF disminuye"? 
> * Con respecto al tiempo, es una duda que planteé en su momento y estoy de acuerdo. Tendremos que consultarlo con Manuel/Paco. Si miras en el apartado 5.1.3 de la ISO 10648-2, se indican 30 minutos ¿?
> *  El tema de igualar las temperaturas, al menos en el Oxygen Method que aplicamos, no sé si es significativo. En la sección 5.1.4 se resalta de este método "the advantage of being not very sensitive to temperature and atmospheric pressure variations". Lo dicho, lo consultamos con Manuel en la reunión.
> * Revisando el estándar no encuentro en qué parte del Oxygen Method se indica que la presión inicial debe bajarse 1000 Pa. Lo que se indica en el punto 5.1.5 es que la variación de la presión atmosférica debe ser menor a 1000 Pa. Es algo que asumimos porque sólo se producen variaciones en las presiones internas. Revisando `calculo_fugas.pdf` tampoco veo dónde "utilizamos" (¿a qué te refieres con utilizamos?) 40 Pa. Necesito más info. o que seas más específico.

2. Para una habitación fija, ¿los cálculos de fugas se consideran para todas en conjunto (una por habitación con la que se conecta) o cada fuga individual?. Supongo que el hourly leak rate es para toda la habitación y habría que sumar las contribuciones de cada fuga o para cada fuga va por separado.
En concreto, me ocurre que la R110 tiene una diferencia entre aire que entra y que sale por el HVAC de unos 2000 m3/h (infiltraciones), lo que hace que en una fuga estándar tenga que llevar el aire a velocidades ultrasónicas (porque las infiltraciones son a través de fugas/puertas no?). Si se pudieran poner fugas por cada conexión, a lo mejor sí es posible. Ahora bien, he echado cuentas generales y, con este caudal, el leak rate sale del orden de 0.2. Lo único que se me ocurriría es no contemplar las puertas como fuga sino como un flujo aparte. Creo que es más adecuado usar el constant pressure method, pues la intención es mantener la diferencia de presión, pero el problema del número de fugas es el mismo.

> ANTONIO: sobre esto, no lo había pensado y comparto la misma duda. Lo consultamos en la reunión.

3. ¿Podríais subir aquí el código original de EAI? ¿Y os vendría bien reuniros la semana que viene para aclarar el tema fugas?

> ANTONIO: te lo paso por mail.
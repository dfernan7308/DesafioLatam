# DesafioLatam

Para el desafio se utilizo python,docker, yaml y AWS para el despliegue de los servicios, dentro del repositorio podran encontrar todos los documentos que se usaron para poder realizar el proyecto.

- Toda la solucion esta alojada en AWS dentro de una VPC dedicada a latam, dentro de estas VPC junto a su security group, ademas se generaron dos subnets privadas junto con su apigateway para lograr tener salida internet desde la instancia ec2, ademas del servicio IAM para la autorizacion de los servicios y su ejecucion.

- Se utilizo el servicio de SQS para poder generar el servicio de mensajeria, para la infraestrcutura se utilizo el servicio de cloud formation, en el cual se le entrego un template completo para poder hacer el despliegue de los demas servicios utilizados.
  
- Para generar de manera efectiva el CI/CD se utilizo el servicio de codepipeline, en donde se genero el sorce y posteriormente el build y deploy del docker que ejecuta la solucion.
  
- Para poder hacer la automatizacion de la solucion se utilizo el servicio de Amazon Elastic Container Registry con esto se genero la imagen la cual genera la URL para poder entregarsela a Cloud formation y asi lograr la comunicacion y generar el task para tener seguridad que funciona la solucion.
  
- El monitoreo y salud de los servicios se utilizo CloudWatch con este servicio se puede revisar el estado del task y asi poder hacer las soluciones en caso de errores.

- Ademas se usaron servicios para ir monitoreando y desarrollando la solucion de manera mas efectiva tales como amazon RDS con la base de datos de postgresql, CodeBuild, Route table y autoscaling.

- Dentro del repositorio existira una carpeta con capturas de pantalla sobre como se ejecutaron de manera efectiva cada servicio de AWS.

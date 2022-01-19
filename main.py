from Bank import CuentaBancaria 

cuenta1=CuentaBancaria().deposito(100).deposito(200).deposito(400).retiro(100).generarInteres().mostrarInfoCuenta()
cuenta2=CuentaBancaria().deposito(200).deposito(300).retiro(20).retiro(50).retiro(60).retiro(10).generarInteres().mostrarInfoCuenta()

CuentaBancaria.imprimirAll()
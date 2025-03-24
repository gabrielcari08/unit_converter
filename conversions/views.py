from django.http import JsonResponse
from django.shortcuts import render

# Diccionario con factores de conversión para longitud
conversion_factors_long = {
    "km": 1000, "hm": 100, "dam": 10, "m": 1, "dm": 0.1, "cm": 0.01, "mm": 0.001
}

# Diccionario con factores de conversión para peso
conversion_factors_weight = {
    "kg": 1000, "hg": 100, "dag": 10, "g": 1, "dg": 0.1, "cg": 0.01, "mg": 0.001
}

def index(request):
    return render(request, 'conversions/index.html')

#------Definicion de conversiones--------

#Convertir longitudes
def convert_long(request):
    if request.method == "GET":  # Verifica si la solicitud es de tipo GET
        value = request.GET.get("value")  # Obtiene el número a convertir
        from_unit = request.GET.get("from")  # Obtiene la unidad de origen
        to_unit = request.GET.get("to")  # Obtiene la unidad de destino

        # Validar que los datos estén presentes
        if not value or not from_unit or not to_unit:
            return JsonResponse({"error": "Faltan parámetros"}, status=400)

        # Intenta convertir el valor almacenado en "value" a float.
        try:
            value = float(value)
        except ValueError:
            return JsonResponse({"error": "El valor debe ser un número"}, status=400)

        # Verificar si las unidades están en el diccionario.
        if from_unit not in conversion_factors_long or to_unit not in conversion_factors_long:
            return JsonResponse({"error": "Unidades no válidas"}, status=400)

        # Realizar la conversión.
        result = value * (conversion_factors_long[from_unit] / conversion_factors_long[to_unit])

        # Devolvemos el resultado en formato JSON
        return JsonResponse({"converted_value": result, "unit": to_unit})

    # Si el usuario utiliza un método distinto al GET, arrojamos este mensaje.
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Convertir peso
def convert_weight(request):
    if request.method == "GET":  # Verifica si la solicitud es de tipo GET
        value = request.GET.get("value")  # Obtiene el número a convertir
        from_unit = request.GET.get("from")  # Obtiene la unidad de origen
        to_unit = request.GET.get("to")  # Obtiene la unidad de destino

        # Validar que los datos estén presentes
        if not value or not from_unit or not to_unit:
            return JsonResponse({"error": "Faltan parámetros"}, status=400)

        # Intenta convertir el valor almacenado en "value" a float.
        try:
            value = float(value)
        except ValueError:
            return JsonResponse({"error": "El valor debe ser un número"}, status=400)

        # Verificar si las unidades están en el diccionario.
        if from_unit not in conversion_factors_weight or to_unit not in conversion_factors_weight:
            return JsonResponse({"error": "Unidades no válidas"}, status=400)

        # Realizar la conversión.
        result = value * (conversion_factors_weight[from_unit] / conversion_factors_weight[to_unit])

        # Devolvemos el resultado en formato JSON
        return JsonResponse({"converted_value": result, "unit": to_unit})

    # Si el usuario utiliza un método distinto al GET, arrojamos este mensaje.
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Convertir temperatura
def convert_temperature(request):
    if request.method == "GET":  # Verifica si la solicitud es de tipo GET
        value = request.GET.get("value")  # Obtiene el número a convertir
        from_unit = request.GET.get("from")  # Obtiene la unidad de origen
        to_unit = request.GET.get("to")  # Obtiene la unidad de destino
        
        # Validar que los datos estén presentes
        if not value or not from_unit or not to_unit:
            return JsonResponse({"error": "Faltan parámetros"}, status=400)
        
        # Intenta convertir el valor almacenado en "value" a float.
        try:
            value = float(value)
        except ValueError:
            return JsonResponse({"error": "El valor debe ser un número"}, status=400)
        
        # Lista de unidades válidas
        valid_units = ["c", "f", "k"]
        
        # Verificar si las unidades están en la lista de unidades válidas.
        if from_unit not in valid_units or to_unit not in valid_units:
            return JsonResponse({"error": "Unidades no válidas"}, status=400)

        # Realizar la conversión de temperatura
        result = None
        if from_unit == "c": 
            if to_unit == "f":
                result = (value * 9/5) + 32
            elif to_unit == "k":
                result = value + 273.15
        elif from_unit == "f":
            if to_unit == "c":
                result = (value - 32) * 5/9
            elif to_unit == "k":
                result = (value + 459.67) * 5/9
        elif from_unit == "k":
            if to_unit == "c":
                result = value - 273.15
            elif to_unit == "f":
                result = (value * 9/5) - 459.67

        # Si no se encontró una conversión válida
        if result is None:
            return JsonResponse({"error": "Conversión no soportada"}, status=400)

        # Devolvemos el resultado en formato JSON
        return JsonResponse({"converted_value": result, "unit": to_unit})

    # Si el usuario utiliza un método distinto al GET, arrojamos este mensaje.
    return JsonResponse({"error": "Método no permitido"}, status=405)

#NOTAS:

# Falta manejar que no se permiten valores negativos en longitud y peso
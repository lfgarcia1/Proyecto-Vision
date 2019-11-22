"""
Template para tomar un algoritmo de detección, procesar un video y crear las carpetas
correspondientes.

Acciones:
    - Cargar video
    - Recorrer frame por frame
    - Posibilidad de cambiar funcion que entregue los bounding boxes
    - [TODO] Guardar bounding boxes segun método (en su carpeta correspondiente)
"""
import cv2
import numpy as np

# Importar metodos de deteccion
from dlib_detector import get_boxes as dlib_boxes
from retinaface_detector import get_boxes as retina_boxes


def process_frame(image, method):
    """
    Procesa frame. Method puede ser 'retinaface' o 'dlib'
    """
    if method == 'dlib':
        faces = dlib_boxes(image)
    elif method == 'retinaface':
        faces = retina_boxes(image)
    else:
        raise NotImplementedError(f'Método {method} no existe')

    # TODO: En el caso que sea un vector, corregir para que sea matriz
    return faces


def process_video(path, method):
    """
    Procesa frame por frame un video. Method puede ser 'retinaface' o 'dlib'
    """
    # TODO: Obtener nombre de video a partir del path
    video_name = ''
    # TODO: Crear carpeta si es que no existe (Deteccion/{method}/{video_name})
    folder_path = f"Deteccion/{method}/{video_name}"
    try:
        cap = cv2.VideoCapture(path)
        # Check if camera opened successfully
        if (cap.isOpened() is False):
            print("Error opening video stream or file")

        frame_counter = 0
        # Read until video is completed
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret is True:
                # TODO: Crear carpeta del frame si es que no existe (Deteccion/{method}/{video_name}/{frame_name})
                frame_name = f"frame_{frame_counter}"

                faces = process_frame(frame, method)
                # TODO: Guardar bounding boxes
                np.save(f"{folder_path}/{frame_name}/bounding_boxes.npy", faces)

                # TODO: Guardar imagenes recortadas
                for bb in faces:
                    pass
                frame_counter += 1

            # Break the loop
            else:
                break

    finally:
        # When everything done, release the video capture object
        cap.release()

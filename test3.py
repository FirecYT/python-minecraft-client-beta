# PyOpenGL Setup
# Ref: https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/

import sys
print('Python version: ' + sys.version + '\n')

import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

print("OpenGL Imports successful!") # If you see this printed to the console then installation was successful

def showScreen():
    return

glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow(b"OpenGL Coding Practice") # Give your window a title

# print OpenGL Driver Information
try:
    # this method can be called only after glutCreateWindow has been called.
    # it works only after a opengl context has been created
    # OpenGL Context: https://www.khronos.org/opengl/wiki/OpenGL_Context

    print("OpenGL Vendor: " + GL.glGetString(GL.GL_VENDOR).decode())
    print("OpenGL Renderer: " + GL.glGetString(GL.GL_RENDERER).decode())
    gl_version_str = GL.glGetString(GL.GL_VERSION)
    gl_version = float(gl_version_str[:3])
    print("OpenGL Renderer Version: " + str(gl_version) + " ( " + gl_version_str.decode() + " )")
    print("OpenGL Shading Language Version: " + GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION).decode())
    print("OpenGL Total Extensions: " + str(GL.glGetIntegerv(GL.GL_NUM_EXTENSIONS)))

    gl_extensions_str = GL.glGetString(GL.GL_EXTENSIONS).decode()

    #print("OpenGL Extensions: " + gl_extensions_str)
    #print("OpenGL ATTRIBUTES:\n",", ".join(d for d in dir(GL) if d.startswith("GL_")))

    vram_total = vram_used = vram_available = 'Unknown'

    # https://gamedev.stackexchange.com/questions/3346/how-can-i-tell-how-much-video-card-memory-im-using
    # Only for Nvidia GPUs
    # https://stackoverflow.com/questions/43267640/how-i-can-get-my-total-gpu-memory-using-qts-native-opengl
    if('GL_NVX_gpu_memory_info' in gl_extensions_str):

        # Ref: https://github.com/collincebecky/QT-OPENCV-GSTREAMER-CUDA/blob/master/glUtility.h
        # https://registry.khronos.org/OpenGL/extensions/NVX/NVX_gpu_memory_info.txt
        GL_GPU_MEM_INFO_TOTAL_AVAILABLE_MEM_NVX = 0x9048
        GL_GPU_MEM_INFO_CURRENT_AVAILABLE_MEM_NVX = 0x9049

        vram_total = GL.glGetIntegerv(GL_GPU_MEM_INFO_TOTAL_AVAILABLE_MEM_NVX)
        vram_available = GL.glGetIntegerv(GL_GPU_MEM_INFO_CURRENT_AVAILABLE_MEM_NVX)
        vram_used = vram_total - vram_available

    # For AMD gpus (Integrated GPUs)
    # https://registry.khronos.org/OpenGL/extensions/ATI/ATI_meminfo.txt
    elif ('GL_ATI_meminfo' in gl_extensions_str):
        TEXTURE_FREE_MEMORY_ATI = 0x87FC
        vram_total = GL.glGetIntegerv(TEXTURE_FREE_MEMORY_ATI)

    else:
        print('Memory information not available')

    print("Total VRAM: " + str( vram_total ) + " KB")
    print("VRAM Used: " + str( vram_used ) + " KB")
    print("Total Available VRAM: " + str( vram_available ) + " KB")

except Exception as e:
    print('GL.glGetString failed:' + str(e))

glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
glutMainLoop()  # Keeps the window created above displaying/running in a loop

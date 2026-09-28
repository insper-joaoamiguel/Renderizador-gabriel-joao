#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# pylint: disable=invalid-name

"""
Biblioteca Gráfica / Graphics Library.

Desenvolvido por: <SEU NOME AQUI>
Disciplina: Computação Gráfica
Data: <DATA DE INÍCIO DA IMPLEMENTAÇÃO>
"""

import time         # Para operações com tempo
import gpu          # Simula os recursos de uma GPU
import math         # Funções matemáticas
import numpy as np  # Biblioteca do Numpy

class GL:
    """Classe que representa a biblioteca gráfica (Graphics Library)."""

    width = 800   # largura da tela
    height = 600  # altura da tela
    near = 0.01   # plano de corte próximo
    far = 1000    # plano de corte distante

    @staticmethod
    def setup(width, height, near=0.01, far=1000):
        """Definr parametros para câmera de razão de aspecto, plano próximo e distante."""
        GL.width = width
        GL.height = height
        GL.near = near
        GL.far = far

    @staticmethod
    def polypoint2D(point, colors):
        """Função usada para renderizar Polypoint2D."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry2D.html#Polypoint2D
        # Nessa função você receberá pontos no parâmetro point, esses pontos são uma lista
        # de pontos x, y sempre na ordem. Assim point[0] é o valor da coordenada x do
        # primeiro ponto, point[1] o valor y do primeiro ponto. Já point[2] é a
        # coordenada x do segundo ponto e assim por diante. Assuma a quantidade de pontos
        # pelo tamanho da lista e assuma que sempre vira uma quantidade par de valores.
        # O parâmetro colors é um dicionário com os tipos cores possíveis, para o Polypoint2D
        # você pode assumir inicialmente o desenho dos pontos com a cor emissiva (emissiveColor).

        # Exemplo:
        pos_x = GL.width//2
        pos_y = GL.height//2
        # gpu.GPU.draw_pixel([pos_x, pos_y], gpu.GPU.RGB8, [255, 0, 0])  # altera pixel (u, v, tipo, r, g, b)
        # cuidado com as cores, o X3D especifica de (0,1) e o Framebuffer de (0,255)

        cores = []
        for c in colors["emissiveColor"]:
            cores.append(int(c*255))

        for i in range(0, len(point) // 2):
            i = i * 2
            px = int(point[i])
            py = int(point[i+1])
            gpu.GPU.draw_pixel([px, py], gpu.GPU.RGB8, cores)            
            

    @staticmethod
    def polyline2D(lineSegments, colors):
        """Função usada para renderizar Polyline2D."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry2D.html#Polyline2D
        # Nessa função você receberá os pontos de uma linha no parâmetro lineSegments, esses
        # pontos são uma lista de pontos x, y sempre na ordem. Assim point[0] é o valor da
        # coordenada x do primeiro ponto, point[1] o valor y do primeiro ponto. Já point[2] é
        # a coordenada x do segundo ponto e assim por diante. Assuma a quantidade de pontos
        # pelo tamanho da lista. A quantidade mínima de pontos são 2 (4 valores), porém a
        # função pode receber mais pontos para desenhar vários segmentos. Assuma que sempre
        # vira uma quantidade par de valores.
        # O parâmetro colors é um dicionário com os tipos cores possíveis, para o Polyline2D
        # você pode assumir inicialmente o desenho das linhas com a cor emissiva (emissiveColor).

        print("Polyline2D : lineSegments = {0}".format(lineSegments)) # imprime no terminal
        print("Polyline2D : colors = {0}".format(colors)) # imprime no terminal as cores
        
        # Exemplo:
        # pos_x = GL.width//2
        # pos_y = GL.height//2
        # gpu.GPU.draw_pixel([pos_x, pos_y], gpu.GPU.RGB8, [255, 0, 255])  # altera pixel (u, v, tipo, r, g, b)
        # cuidado com as cores, o X3D especifica de (0,1) e o Framebuffer de (0,255)

        cores = []
        for c in colors['emissiveColor']:
            cores.append(int(c*255))

        for i in range(0, len(lineSegments) - 2, 2):
            x0, y0 = lineSegments[i], lineSegments[i + 1]
            x1, y1 = lineSegments[i + 2], lineSegments[i + 3]

            dx = x1 - x0
            dy = y1 - y0

            if abs(dx) >= abs(dy):
                if x0 > x1:
                    x0, y0, x1, y1 = x1, y1, x0, y0

                s = (y1 - y0) / (x1 - x0)
                for u in range(int(x0), int(x1) + 1):
                    v = y0 + s * (u - x0)
                    try:
                        gpu.GPU.draw_pixel([u, int(v)], gpu.GPU.RGB8, cores)
                    except Exception:
                        pass

            else:
                if y0 > y1:
                    x0, y0, x1, y1 = x1, y1, x0, y0

                s = (x1 - x0) / (y1 - y0)
                for u in range(int(y0), int(y1) + 1):
                    v = x0 + s * (u - y0)
                    try:
                        gpu.GPU.draw_pixel([int(v), u], gpu.GPU.RGB8, cores)
                    except Exception:
                        pass
                


    @staticmethod
    def circle2D(radius, colors):
        """Função usada para renderizar Circle2D."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry2D.html#Circle2D
        # Nessa função você receberá um valor de raio e deverá desenhar o contorno de
        # um círculo.
        # O parâmetro colors é um dicionário com os tipos cores possíveis, para o Circle2D
        # você pode assumir o desenho das linhas com a cor emissiva (emissiveColor).

        print("Circle2D : radius = {0}".format(radius)) # imprime no terminal
        print("Circle2D : colors = {0}".format(colors)) # imprime no terminal as cores
        
        # Exemplo:
        pos_x = GL.width//2
        pos_y = GL.height//2
        gpu.GPU.draw_pixel([pos_x, pos_y], gpu.GPU.RGB8, [255, 0, 255])  # altera pixel (u, v, tipo, r, g, b)
        # cuidado com as cores, o X3D especifica de (0,1) e o Framebuffer de (0,255)


    @staticmethod
    def triangleSet2D(vertices, colors):
        """Função usada para renderizar TriangleSet2D."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry2D.html#TriangleSet2D
        # Nessa função você receberá os vertices de um triângulo no parâmetro vertices,
        # esses pontos são uma lista de pontos x, y sempre na ordem. Assim point[0] é o
        # valor da coordenada x do primeiro ponto, point[1] o valor y do primeiro ponto.
        # Já point[2] é a coordenada x do segundo ponto e assim por diante. Assuma que a
        # quantidade de pontos é sempre multiplo de 3, ou seja, 6 valores ou 12 valores, etc.
        # O parâmetro colors é um dicionário com os tipos cores possíveis, para o TriangleSet2D
        # você pode assumir inicialmente o desenho das linhas com a cor emissiva (emissiveColor).
        print("TriangleSet2D : vertices = {0}".format(vertices)) # imprime no terminal
        print("TriangleSet2D : colors = {0}".format(colors)) # imprime no terminal as cores

        # Exemplo:
        # gpu.GPU.draw_pixel([6, 8], gpu.GPU.RGB8, [255, 255, 0])  # altera pixel (u, v, tipo, r, g, b)

        cores = []
        for c in colors["emissiveColor"]:
            cores.append(int(c*255))

        def L(ax, ay, bx, by, x, y):
            return ((by - ay) * x
                    - (bx - ax) * y
                    + ay * (bx - ax)
                    - ax * (by - ay))
        
        for i in range(0, len(vertices), 6):

            x0 = vertices[i]
            y0 = vertices[i + 1]

            x1 = vertices[i + 2]
            y1 = vertices[i + 3]

            x2 = vertices[i + 4]
            y2 = vertices[i + 5]

            xmin = max(0, int(min(x0, x1, x2)))
            xmax = min(GL.width - 1, int(max(x0, x1, x2)))

            ymin = max(0, int(min(y0, y1, y2)))
            ymax = min(GL.height - 1, int(max(y0, y1, y2)))


            for px in range(xmin, xmax + 1):
                for py in range(ymin, ymax + 1):

                    sx = px + 0.5
                    sy = py + 0.5

                    l0 = L(x0, y0, x1, y1, sx, sy)
                    l1 = L(x1, y1, x2, y2, sx, sy)
                    l2 = L(x2, y2, x0, y0, sx, sy)

                    if ((l0 >= 0 and l1 >= 0 and l2 >= 0) or
                        (l0 <= 0 and l1 <= 0 and l2 <= 0)):

                        gpu.GPU.draw_pixel([px, py], gpu.GPU.RGB8, cores)

        


    @staticmethod
    def triangleSet(point, colors):
        """Função usada para renderizar TriangleSet."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/rendering.html#TriangleSet
        # Nessa função você receberá pontos no parâmetro point, esses pontos são uma lista
        # de pontos x, y, e z sempre na ordem. Assim point[0] é o valor da coordenada x do
        # primeiro ponto, point[1] o valor y do primeiro ponto, point[2] o valor z da
        # coordenada z do primeiro ponto. Já point[3] é a coordenada x do segundo ponto e
        # assim por diante.
        # No TriangleSet os triângulos são informados individualmente, assim os três
        # primeiros pontos definem um triângulo, os três próximos pontos definem um novo
        # triângulo, e assim por diante.
        # O parâmetro colors é um dicionário com os tipos cores possíveis, você pode assumir
        # inicialmente, para o TriangleSet, o desenho das linhas com a cor emissiva
        # (emissiveColor), conforme implementar novos materias você deverá suportar outros
        # tipos de cores.

        # Exemplo de desenho de um pixel branco na coordenada 10, 10
        # gpu.GPU.draw_pixel([10, 10], gpu.GPU.RGB8, [255, 255, 255])  # altera pixel

        def barycentric(vertices, x, y):
            x0, y0 = vertices[0]
            x1, y1 = vertices[1]
            x2, y2 = vertices[2]
            denominator = ((y1 - y2) * (x0 - x2)
                           + (x2 - x1) * (y0 - y2))
            if abs(denominator) <= 1e-12:
                return None
            l0 = ((y1 - y2) * (x - x2)
                  + (x2 - x1) * (y - y2)) / denominator
            l1 = ((y2 - y0) * (x - x2)
                  + (x0 - x2) * (y - y2)) / denominator
            return np.array([l0, l1, 1.0 - l0 - l1], dtype=float)

        view_matrix = getattr(GL, "view_matrix", np.identity(4))
        perspective_matrix = getattr(GL, "perspective_matrix", np.identity(4))
        model_matrix = getattr(GL, "transform_matrix", np.identity(4))
        mvp = perspective_matrix @ view_matrix @ model_matrix
        aspect = GL.width / GL.height

        projected = []
        for offset in range(0, len(point), 3):
            vertex = np.array([
                point[offset], point[offset + 1], point[offset + 2], 1.0
            ])
            clip = mvp @ vertex
            if clip[3] <= 1e-12:
                projected.append(None)
                continue
            ndc = clip[:3] / clip[3]

            # viewpoint() trata o fieldOfView como o menor ângulo. Esta
            # compensação mantém a razão de aspecto dos exemplos.
            if aspect > 1.0:
                ndc[0] /= aspect
                ndc[1] /= aspect

            projected.append({
                "screen": np.array([
                    (ndc[0] + 1.0) * 0.5 * GL.width,
                    (1.0 - ndc[1]) * 0.5 * GL.height,
                ]),
                "depth": float(ndc[2]),
            })

        source_color = np.clip(
            np.asarray(colors["emissiveColor"], dtype=float), 0.0, 1.0
        ) * 255.0
        opacity = 1.0 - min(max(float(colors["transparency"]), 0.0), 1.0)

        for first in range(0, len(projected) - 2, 3):
            triangle = projected[first:first + 3]
            if any(vertex is None for vertex in triangle):
                continue

            screen = np.asarray(
                [vertex["screen"] for vertex in triangle], dtype=float
            )
            depths = np.asarray(
                [vertex["depth"] for vertex in triangle], dtype=float
            )
            if barycentric(screen, screen[0, 0], screen[0, 1]) is None:
                continue

            xmin = max(0, int(math.floor(np.min(screen[:, 0]))))
            xmax = min(GL.width - 1, int(math.ceil(np.max(screen[:, 0]))))
            ymin = max(0, int(math.floor(np.min(screen[:, 1]))))
            ymax = min(GL.height - 1, int(math.ceil(np.max(screen[:, 1]))))

            for py in range(ymin, ymax + 1):
                for px in range(xmin, xmax + 1):
                    weights = barycentric(screen, px + 0.5, py + 0.5)
                    if weights is None or np.min(weights) < -1e-9:
                        continue

                    fragment_depth = float(np.dot(weights, depths))
                    if fragment_depth < -1.0 or fragment_depth > 1.0:
                        continue
                    stored_depth = float(gpu.GPU.read_pixel(
                        [px, py], gpu.GPU.DEPTH_COMPONENT32F
                    )[0])
                    if fragment_depth >= stored_depth - 1e-7:
                        continue

                    destination = np.asarray(
                        gpu.GPU.read_pixel([px, py], gpu.GPU.RGB8),
                        dtype=float,
                    )
                    blended = (source_color * opacity
                               + destination * (1.0 - opacity))
                    output = np.rint(
                        np.clip(blended, 0.0, 255.0)
                    ).astype(int).tolist()
                    gpu.GPU.draw_pixel([px, py], gpu.GPU.RGB8, output)
                    gpu.GPU.draw_pixel(
                        [px, py],
                        gpu.GPU.DEPTH_COMPONENT32F,
                        [fragment_depth],
                    )



    @staticmethod
    def viewpoint(position, orientation, fieldOfView):
        """Função usada para renderizar (na verdade coletar os dados) de Viewpoint."""
        # Na função de viewpoint você receberá a posição, orientação e campo de visão da
        # câmera virtual. Use esses dados para poder calcular e criar a matriz de projeção
        # perspectiva para poder aplicar nos pontos dos objetos geométricos.

        def rotation_matrix(x, y, z, angle):
            axis = np.array([x, y, z], dtype=float)
            norm = np.linalg.norm(axis)
            if norm > 1e-8:
                axis = axis / norm
            x, y, z = axis
            c, s, t = math.cos(angle), math.sin(angle), 1 - math.cos(angle)
            R = np.identity(4)
            R[0, 0] = t*x*x + c
            R[0, 1] = t*x*y - s*z
            R[0, 2] = t*x*z + s*y
            R[1, 0] = t*x*y + s*z
            R[1, 1] = t*y*y + c
            R[1, 2] = t*y*z - s*x
            R[2, 0] = t*x*z - s*y
            R[2, 1] = t*y*z + s*x
            R[2, 2] = t*z*z + c
            return R

        T = np.identity(4)
        T[0, 3], T[1, 3], T[2, 3] = position[0], position[1], position[2]

        R = rotation_matrix(orientation[0], orientation[1], orientation[2], orientation[3])

        camera_matrix = T @ R

        # Guarda o estado como atributo dinâmico da classe GL
        setattr(GL, "view_matrix", np.linalg.inv(camera_matrix))

        aspect = GL.width / GL.height
        fovy = fieldOfView
        if aspect > 1:
            fovy = 2 * math.atan(math.tan(fieldOfView / 2) / aspect)

        f = 1.0 / math.tan(fovy / 2)
        near, far = GL.near, GL.far

        P = np.zeros((4, 4))
        P[0, 0] = f / aspect
        P[1, 1] = f
        P[2, 2] = (far + near) / (near - far)
        P[2, 3] = (2 * far * near) / (near - far)
        P[3, 2] = -1

        setattr(GL, "perspective_matrix", P)

    @staticmethod
    def transform_in(translation, scale, rotation):
        """Função usada para renderizar (na verdade coletar os dados) de Transform."""
        # A função transform_in será chamada quando se entrar em um nó X3D do tipo Transform
        # do grafo de cena. Os valores passados são a escala em um vetor [x, y, z]
        # indicando a escala em cada direção, a translação [x, y, z] nas respectivas
        # coordenadas e finalmente a rotação por [x, y, z, t] sendo definida pela rotação
        # do objeto ao redor do eixo x, y, z por t radianos, seguindo a regra da mão direita.
        # ESSES NÃO SÃO OS VALORES DE QUATÉRNIOS AS CONTAS AINDA PRECISAM SER FEITAS.
        # Quando se entrar em um nó transform se deverá salvar a matriz de transformação dos
        # modelos do mundo para depois potencialmente usar em outras chamadas. 
        # Quando começar a usar Transforms dentre de outros Transforms, mais a frente no curso
        # Você precisará usar alguma estrutura de dados pilha para organizar as matrizes.

        def rotation_matrix(x, y, z, angle):
            axis = np.array([x, y, z], dtype=float)
            norm = np.linalg.norm(axis)
            if norm > 1e-8:
                axis = axis / norm
            x, y, z = axis
            c, s, t = math.cos(angle), math.sin(angle), 1 - math.cos(angle)
            R = np.identity(4)
            R[0, 0] = t*x*x + c
            R[0, 1] = t*x*y - s*z
            R[0, 2] = t*x*z + s*y
            R[1, 0] = t*x*y + s*z
            R[1, 1] = t*y*y + c
            R[1, 2] = t*y*z - s*x
            R[2, 0] = t*x*z - s*y
            R[2, 1] = t*y*z + s*x
            R[2, 2] = t*z*z + c
            return R

        T = np.identity(4)
        S = np.identity(4)
        R = np.identity(4)

        if translation:
            T[0, 3], T[1, 3], T[2, 3] = translation[0], translation[1], translation[2]
        if scale:
            S[0, 0], S[1, 1], S[2, 2] = scale[0], scale[1], scale[2]
        if rotation:
            R = rotation_matrix(rotation[0], rotation[1], rotation[2], rotation[3])

        model = T @ R @ S

        # SEM pilha: sobrescreve a matriz atual
        setattr(GL, "transform_matrix", model)

    @staticmethod
    def transform_out():
        """Função usada para renderizar (na verdade coletar os dados) de Transform."""
        # A função transform_out será chamada quando se sair em um nó X3D do tipo Transform do
        # grafo de cena. Não são passados valores, porém quando se sai de um nó transform se
        # deverá recuperar a matriz de transformação dos modelos do mundo da estrutura de
        # pilha implementada.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("Saindo de Transform")

    @staticmethod
    def triangleStripSet(point, stripCount, colors):
        """Função usada para renderizar TriangleStripSet."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/rendering.html#TriangleStripSet
        # A função triangleStripSet é usada para desenhar tiras de triângulos interconectados,
        # você receberá as coordenadas dos pontos no parâmetro point, esses pontos são uma
        # lista de pontos x, y, e z sempre na ordem. Assim point[0] é o valor da coordenada x
        # do primeiro ponto, point[1] o valor y do primeiro ponto, point[2] o valor z da
        # coordenada z do primeiro ponto. Já point[3] é a coordenada x do segundo ponto e assim
        # por diante. No TriangleStripSet a quantidade de vértices a serem usados é informado
        # em uma lista chamada stripCount (perceba que é uma lista). Ligue os vértices na ordem,
        # primeiro triângulo será com os vértices 0, 1 e 2, depois serão os vértices 1, 2 e 3,
        # depois 2, 3 e 4, e assim por diante. Cuidado com a orientação dos vértices, ou seja,
        # todos no sentido horário ou todos no sentido anti-horário, conforme especificado.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("TriangleStripSet : pontos = {0} ".format(point), end='')
        for i, strip in enumerate(stripCount):
            print("strip[{0}] = {1} ".format(i, strip), end='')
        print("")
        print("TriangleStripSet : colors = {0}".format(colors)) # imprime no terminal as cores

        # Exemplo de desenho de um pixel branco na coordenada 10, 10
        gpu.GPU.draw_pixel([10, 10], gpu.GPU.RGB8, [255, 255, 255])  # altera pixel

    @staticmethod
    def indexedTriangleStripSet(point, index, colors):
        """Função usada para renderizar IndexedTriangleStripSet."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/rendering.html#IndexedTriangleStripSet
        # A função indexedTriangleStripSet é usada para desenhar tiras de triângulos
        # interconectados, você receberá as coordenadas dos pontos no parâmetro point, esses
        # pontos são uma lista de pontos x, y, e z sempre na ordem. Assim point[0] é o valor
        # da coordenada x do primeiro ponto, point[1] o valor y do primeiro ponto, point[2]
        # o valor z da coordenada z do primeiro ponto. Já point[3] é a coordenada x do
        # segundo ponto e assim por diante. No IndexedTriangleStripSet uma lista informando
        # como conectar os vértices é informada em index, o valor -1 indica que a lista
        # acabou. A ordem de conexão será de 3 em 3 pulando um índice. Por exemplo: o
        # primeiro triângulo será com os vértices 0, 1 e 2, depois serão os vértices 1, 2 e 3,
        # depois 2, 3 e 4, e assim por diante. Cuidado com a orientação dos vértices, ou seja,
        # todos no sentido horário ou todos no sentido anti-horário, conforme especificado.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("IndexedTriangleStripSet : pontos = {0}, index = {1}".format(point, index))
        print("IndexedTriangleStripSet : colors = {0}".format(colors)) # imprime as cores

        # Exemplo de desenho de um pixel branco na coordenada 10, 10
        gpu.GPU.draw_pixel([10, 10], gpu.GPU.RGB8, [255, 255, 255])  # altera pixel

    @staticmethod
    def indexedFaceSet(coord, coordIndex, colorPerVertex, color, colorIndex,
                       texCoord, texCoordIndex, colors, current_texture):
        """Função usada para renderizar IndexedFaceSet."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry3D.html#IndexedFaceSet
        # A função indexedFaceSet é usada para desenhar malhas de triângulos. Ela funciona de
        # forma muito simular a IndexedTriangleStripSet porém com mais recursos.
        # Você receberá as coordenadas dos pontos no parâmetro cord, esses
        # pontos são uma lista de pontos x, y, e z sempre na ordem. Assim coord[0] é o valor
        # da coordenada x do primeiro ponto, coord[1] o valor y do primeiro ponto, coord[2]
        # o valor z da coordenada z do primeiro ponto. Já coord[3] é a coordenada x do
        # segundo ponto e assim por diante. No IndexedFaceSet uma lista de vértices é informada
        # em coordIndex, o valor -1 indica que a lista acabou.
        # A ordem de conexão não possui uma ordem oficial, mas em geral se o primeiro ponto com os dois
        # seguintes e depois este mesmo primeiro ponto com o terçeiro e quarto ponto. Por exemplo: numa
        # sequencia 0, 1, 2, 3, 4, -1 o primeiro triângulo será com os vértices 0, 1 e 2, depois serão
        # os vértices 0, 2 e 3, e depois 0, 3 e 4, e assim por diante, até chegar no final da lista.
        # Adicionalmente essa implementação do IndexedFace aceita cores por vértices, assim
        # se a flag colorPerVertex estiver habilitada, os vértices também possuirão cores
        # que servem para definir a cor interna dos poligonos, para isso faça um cálculo
        # baricêntrico de que cor deverá ter aquela posição. Da mesma forma se pode definir uma
        # textura para o poligono, para isso, use as coordenadas de textura e depois aplique a
        # cor da textura conforme a posição do mapeamento. Dentro da classe GPU já está
        # implementadado um método para a leitura de imagens.

        def split_faces(indices):
            faces, face = [], []
            for index in indices:
                if index == -1:
                    if face:
                        faces.append(face)
                        face = []
                else:
                    face.append(index)
            if face:
                faces.append(face)
            return faces

        def barycentric(vertices, x, y):
            x0, y0 = vertices[0]
            x1, y1 = vertices[1]
            x2, y2 = vertices[2]
            denominator = ((y1 - y2) * (x0 - x2)
                           + (x2 - x1) * (y0 - y2))
            if abs(denominator) <= 1e-12:
                return None
            l0 = ((y1 - y2) * (x - x2)
                  + (x2 - x1) * (y - y2)) / denominator
            l1 = ((y2 - y0) * (x - x2)
                  + (x0 - x2) * (y - y2)) / denominator
            return np.array([l0, l1, 1.0 - l0 - l1], dtype=float)

        def perspective(values, weights, inv_w):
            corrected = weights * inv_w
            denominator = float(np.sum(corrected))
            if abs(denominator) <= 1e-12:
                return None
            return np.sum(
                values * corrected[:, None], axis=0
            ) / denominator

        def project(points):
            view_matrix = getattr(GL, "view_matrix", np.identity(4))
            perspective_matrix = getattr(
                GL, "perspective_matrix", np.identity(4)
            )
            model_matrix = getattr(GL, "transform_matrix", np.identity(4))
            mvp = perspective_matrix @ view_matrix @ model_matrix
            aspect = GL.width / GL.height
            result = []
            for offset in range(0, len(points), 3):
                vertex = np.array([
                    points[offset], points[offset + 1], points[offset + 2], 1.0
                ])
                clip = mvp @ vertex
                if clip[3] <= 1e-12:
                    result.append(None)
                    continue
                ndc = clip[:3] / clip[3]
                if aspect > 1.0:
                    ndc[0] /= aspect
                    ndc[1] /= aspect
                result.append({
                    "screen": np.array([
                        (ndc[0] + 1.0) * 0.5 * GL.width,
                        (1.0 - ndc[1]) * 0.5 * GL.height,
                    ]),
                    "depth": float(ndc[2]),
                    "inv_w": 1.0 / float(clip[3]),
                })
            return result

        def make_mipmaps(texture_name):
            cache = getattr(GL, "_texture_cache", {})
            key = (gpu.GPU.path, texture_name)
            if key in cache:
                return cache[key]

            # load_texture() entrega a matriz indexada por [u][v].
            image = np.swapaxes(gpu.GPU.load_texture(texture_name), 0, 1)
            if image.ndim == 2:
                image = np.repeat(image[:, :, None], 3, axis=2)
            elif image.shape[2] == 2:
                image = np.concatenate([
                    np.repeat(image[:, :, :1], 3, axis=2),
                    image[:, :, 1:2],
                ], axis=2)
            elif image.shape[2] > 4:
                image = image[:, :, :4]

            levels = [image.astype(np.float32)]
            while levels[-1].shape[0] > 1 or levels[-1].shape[1] > 1:
                current = levels[-1]
                height, width = current.shape[:2]
                padded = np.pad(
                    current,
                    ((0, height % 2), (0, width % 2), (0, 0)),
                    mode="edge",
                )
                levels.append(padded.reshape(
                    padded.shape[0] // 2, 2,
                    padded.shape[1] // 2, 2,
                    padded.shape[2],
                ).mean(axis=(1, 3)))

            cache[key] = levels
            GL._texture_cache = cache
            return levels

        def sample_level(image, uv):
            height, width = image.shape[:2]
            u = min(max(float(uv[0]), 0.0), 1.0)
            v = min(max(float(uv[1]), 0.0), 1.0)
            x = u * (width - 1)
            y = (1.0 - v) * (height - 1)
            x0, y0 = int(math.floor(x)), int(math.floor(y))
            x1, y1 = min(x0 + 1, width - 1), min(y0 + 1, height - 1)
            tx, ty = x - x0, y - y0
            top = image[y0, x0] * (1.0 - tx) + image[y0, x1] * tx
            bottom = image[y1, x0] * (1.0 - tx) + image[y1, x1] * tx
            return top * (1.0 - ty) + bottom * ty

        def sample_texture(levels, uv, lod):
            lod = min(max(float(lod), 0.0), len(levels) - 1)
            first = int(math.floor(lod))
            second = min(first + 1, len(levels) - 1)
            fraction = lod - first
            sample = (sample_level(levels[first], uv) * (1.0 - fraction)
                      + sample_level(levels[second], uv) * fraction)
            if sample.shape[0] >= 4:
                return sample[:3], float(sample[3]) / 255.0
            return sample[:3], 1.0

        def rasterize(vertices, vertex_colors, texture_coordinates, levels):
            if any(vertex is None for vertex in vertices):
                return

            screen = np.asarray(
                [vertex["screen"] for vertex in vertices], dtype=float
            )
            depths = np.asarray(
                [vertex["depth"] for vertex in vertices], dtype=float
            )
            inv_w = np.asarray(
                [vertex["inv_w"] for vertex in vertices], dtype=float
            )
            if barycentric(screen, screen[0, 0], screen[0, 1]) is None:
                return

            xmin = max(0, int(math.floor(np.min(screen[:, 0]))))
            xmax = min(GL.width - 1, int(math.ceil(np.max(screen[:, 0]))))
            ymin = max(0, int(math.floor(np.min(screen[:, 1]))))
            ymax = min(GL.height - 1, int(math.ceil(np.max(screen[:, 1]))))

            delta_x = delta_y = None
            if texture_coordinates is not None and levels:
                origin = barycentric(screen, 0.0, 0.0)
                rate = getattr(GL, "sample_rate", 2)
                delta_x = barycentric(screen, rate, 0.0) - origin
                delta_y = barycentric(screen, 0.0, rate) - origin

            material_color = np.clip(
                np.asarray(colors["emissiveColor"], dtype=float), 0.0, 1.0
            ) * 255.0
            opacity = 1.0 - min(
                max(float(colors["transparency"]), 0.0), 1.0
            )

            for py in range(ymin, ymax + 1):
                for px in range(xmin, xmax + 1):
                    weights = barycentric(screen, px + 0.5, py + 0.5)
                    if weights is None or np.min(weights) < -1e-9:
                        continue

                    fragment_depth = float(np.dot(weights, depths))
                    if fragment_depth < -1.0 or fragment_depth > 1.0:
                        continue
                    stored_depth = float(gpu.GPU.read_pixel(
                        [px, py], gpu.GPU.DEPTH_COMPONENT32F
                    )[0])
                    if fragment_depth >= stored_depth - 1e-7:
                        continue

                    fragment_color = material_color
                    fragment_opacity = opacity
                    if vertex_colors is not None:
                        interpolated = perspective(vertex_colors, weights, inv_w)
                        if interpolated is None:
                            continue
                        fragment_color = np.clip(
                            interpolated, 0.0, 1.0
                        ) * 255.0

                    if texture_coordinates is not None and levels:
                        uv = perspective(texture_coordinates, weights, inv_w)
                        uv_x = perspective(
                            texture_coordinates, weights + delta_x, inv_w
                        )
                        uv_y = perspective(
                            texture_coordinates, weights + delta_y, inv_w
                        )
                        if uv is None or uv_x is None or uv_y is None:
                            continue

                        tex_height, tex_width = levels[0].shape[:2]
                        dx = np.array([
                            (uv_x[0] - uv[0]) * tex_width,
                            (uv_x[1] - uv[1]) * tex_height,
                        ])
                        dy = np.array([
                            (uv_y[0] - uv[0]) * tex_width,
                            (uv_y[1] - uv[1]) * tex_height,
                        ])
                        footprint = max(
                            np.linalg.norm(dx), np.linalg.norm(dy), 1.0
                        )
                        texture_color, texture_alpha = sample_texture(
                            levels, uv, math.log2(footprint)
                        )
                        if vertex_colors is not None:
                            fragment_color = (
                                texture_color * fragment_color / 255.0
                            )
                        else:
                            fragment_color = texture_color
                        fragment_opacity *= texture_alpha

                    destination = np.asarray(
                        gpu.GPU.read_pixel([px, py], gpu.GPU.RGB8), dtype=float
                    )
                    blended = (fragment_color * fragment_opacity
                               + destination * (1.0 - fragment_opacity))
                    output = np.rint(
                        np.clip(blended, 0.0, 255.0)
                    ).astype(int).tolist()
                    gpu.GPU.draw_pixel([px, py], gpu.GPU.RGB8, output)
                    gpu.GPU.draw_pixel(
                        [px, py], gpu.GPU.DEPTH_COMPONENT32F, [fragment_depth]
                    )

        if coord is None or not coord or not coordIndex:
            return

        projected = project(coord)
        coordinate_faces = split_faces(coordIndex)
        color_faces = split_faces(colorIndex) if colorIndex else []
        texture_faces = split_faces(texCoordIndex) if texCoordIndex else []
        color_values = (np.asarray(color, dtype=float).reshape((-1, 3))
                        if color else None)
        texture_values = (np.asarray(texCoord, dtype=float).reshape((-1, 2))
                          if texCoord else None)
        levels = None
        if current_texture and texture_values is not None:
            levels = make_mipmaps(current_texture[0])

        flat_color_indices = [value for value in colorIndex if value != -1]
        for face_number, coordinate_face in enumerate(coordinate_faces):
            if len(coordinate_face) < 3:
                continue

            if colorPerVertex:
                vertex_color_indices = coordinate_face
                if face_number < len(color_faces):
                    vertex_color_indices = color_faces[face_number]
                face_color_index = None
            else:
                vertex_color_indices = None
                face_color_index = (flat_color_indices[face_number]
                                    if face_number < len(flat_color_indices)
                                    else face_number)

            texture_face = (texture_faces[face_number]
                            if face_number < len(texture_faces)
                            else coordinate_face)

            for corner in range(1, len(coordinate_face) - 1):
                local_indices = [0, corner, corner + 1]
                coordinate_indices = [
                    coordinate_face[index] for index in local_indices
                ]
                if any(index < 0 or index >= len(projected)
                       for index in coordinate_indices):
                    continue
                vertices = [projected[index] for index in coordinate_indices]

                triangle_colors = None
                if color_values is not None:
                    if colorPerVertex:
                        if max(local_indices) >= len(vertex_color_indices):
                            continue
                        indices = [
                            vertex_color_indices[index]
                            for index in local_indices
                        ]
                        if any(index < 0 or index >= len(color_values)
                               for index in indices):
                            continue
                        triangle_colors = color_values[indices]
                    elif 0 <= face_color_index < len(color_values):
                        triangle_colors = np.repeat(
                            color_values[face_color_index][None, :], 3, axis=0
                        )

                triangle_texcoords = None
                if (texture_values is not None
                        and len(texture_face) > max(local_indices)):
                    indices = [texture_face[index] for index in local_indices]
                    if all(0 <= index < len(texture_values)
                           for index in indices):
                        triangle_texcoords = texture_values[indices]

                rasterize(
                    vertices, triangle_colors, triangle_texcoords, levels
                )

    @staticmethod
    def box(size, colors):
        """Função usada para renderizar Boxes."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry3D.html#Box
        # A função box é usada para desenhar paralelepípedos na cena. O Box é centrada no
        # (0, 0, 0) no sistema de coordenadas local e alinhado com os eixos de coordenadas
        # locais. O argumento size especifica as extensões da caixa ao longo dos eixos X, Y
        # e Z, respectivamente, e cada valor do tamanho deve ser maior que zero. Para desenha
        # essa caixa você vai provavelmente querer tesselar ela em triângulos, para isso
        # encontre os vértices e defina os triângulos.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("Box : size = {0}".format(size)) # imprime no terminal pontos
        print("Box : colors = {0}".format(colors)) # imprime no terminal as cores

        # Exemplo de desenho de um pixel branco na coordenada 10, 10
        gpu.GPU.draw_pixel([10, 10], gpu.GPU.RGB8, [255, 255, 255])  # altera pixel

    @staticmethod
    def sphere(radius, colors):
        """Função usada para renderizar Esferas."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry3D.html#Sphere
        # A função sphere é usada para desenhar esferas na cena. O esfera é centrada no
        # (0, 0, 0) no sistema de coordenadas local. O argumento radius especifica o
        # raio da esfera que está sendo criada. Para desenha essa esfera você vai
        # precisar tesselar ela em triângulos, para isso encontre os vértices e defina
        # os triângulos.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("Sphere : radius = {0}".format(radius)) # imprime no terminal o raio da esfera
        print("Sphere : colors = {0}".format(colors)) # imprime no terminal as cores

    @staticmethod
    def cone(bottomRadius, height, colors):
        """Função usada para renderizar Cones."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry3D.html#Cone
        # A função cone é usada para desenhar cones na cena. O cone é centrado no
        # (0, 0, 0) no sistema de coordenadas local. O argumento bottomRadius especifica o
        # raio da base do cone e o argumento height especifica a altura do cone.
        # O cone é alinhado com o eixo Y local. O cone é fechado por padrão na base.
        # Para desenha esse cone você vai precisar tesselar ele em triângulos, para isso
        # encontre os vértices e defina os triângulos.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("Cone : bottomRadius = {0}".format(bottomRadius)) # imprime no terminal o raio da base do cone
        print("Cone : height = {0}".format(height)) # imprime no terminal a altura do cone
        print("Cone : colors = {0}".format(colors)) # imprime no terminal as cores

    @staticmethod
    def cylinder(radius, height, colors):
        """Função usada para renderizar Cilindros."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/geometry3D.html#Cylinder
        # A função cylinder é usada para desenhar cilindros na cena. O cilindro é centrado no
        # (0, 0, 0) no sistema de coordenadas local. O argumento radius especifica o
        # raio da base do cilindro e o argumento height especifica a altura do cilindro.
        # O cilindro é alinhado com o eixo Y local. O cilindro é fechado por padrão em ambas as extremidades.
        # Para desenha esse cilindro você vai precisar tesselar ele em triângulos, para isso
        # encontre os vértices e defina os triângulos.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("Cylinder : radius = {0}".format(radius)) # imprime no terminal o raio do cilindro
        print("Cylinder : height = {0}".format(height)) # imprime no terminal a altura do cilindro
        print("Cylinder : colors = {0}".format(colors)) # imprime no terminal as cores

    @staticmethod
    def navigationInfo(headlight):
        """Características físicas do avatar do visualizador e do modelo de visualização."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/navigation.html#NavigationInfo
        # O campo do headlight especifica se um navegador deve acender um luz direcional que
        # sempre aponta na direção que o usuário está olhando. Definir este campo como TRUE
        # faz com que o visualizador forneça sempre uma luz do ponto de vista do usuário.
        # A luz headlight deve ser direcional, ter intensidade = 1, cor = (1 1 1),
        # ambientIntensity = 0,0 e direção = (0 0 −1).

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("NavigationInfo : headlight = {0}".format(headlight)) # imprime no terminal

    @staticmethod
    def directionalLight(ambientIntensity, color, intensity, direction):
        """Luz direcional ou paralela."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/lighting.html#DirectionalLight
        # Define uma fonte de luz direcional que ilumina ao longo de raios paralelos
        # em um determinado vetor tridimensional. Possui os campos básicos ambientIntensity,
        # cor, intensidade. O campo de direção especifica o vetor de direção da iluminação
        # que emana da fonte de luz no sistema de coordenadas local. A luz é emitida ao
        # longo de raios paralelos de uma distância infinita.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("DirectionalLight : ambientIntensity = {0}".format(ambientIntensity))
        print("DirectionalLight : color = {0}".format(color)) # imprime no terminal
        print("DirectionalLight : intensity = {0}".format(intensity)) # imprime no terminal
        print("DirectionalLight : direction = {0}".format(direction)) # imprime no terminal

    @staticmethod
    def pointLight(ambientIntensity, color, intensity, location):
        """Luz pontual."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/lighting.html#PointLight
        # Fonte de luz pontual em um local 3D no sistema de coordenadas local. Uma fonte
        # de luz pontual emite luz igualmente em todas as direções; ou seja, é omnidirecional.
        # Possui os campos básicos ambientIntensity, cor, intensidade. Um nó PointLight ilumina
        # a geometria em um raio de sua localização. O campo do raio deve ser maior ou igual a
        # zero. A iluminação do nó PointLight diminui com a distância especificada.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("PointLight : ambientIntensity = {0}".format(ambientIntensity))
        print("PointLight : color = {0}".format(color)) # imprime no terminal
        print("PointLight : intensity = {0}".format(intensity)) # imprime no terminal
        print("PointLight : location = {0}".format(location)) # imprime no terminal

    @staticmethod
    def fog(visibilityRange, color):
        """Névoa."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/environmentalEffects.html#Fog
        # O nó Fog fornece uma maneira de simular efeitos atmosféricos combinando objetos
        # com a cor especificada pelo campo de cores com base nas distâncias dos
        # vários objetos ao visualizador. A visibilidadeRange especifica a distância no
        # sistema de coordenadas local na qual os objetos são totalmente obscurecidos
        # pela névoa. Os objetos localizados fora de visibilityRange do visualizador são
        # desenhados com uma cor de cor constante. Objetos muito próximos do visualizador
        # são muito pouco misturados com a cor do nevoeiro.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("Fog : color = {0}".format(color)) # imprime no terminal
        print("Fog : visibilityRange = {0}".format(visibilityRange))

    @staticmethod
    def timeSensor(cycleInterval, loop):
        """Gera eventos conforme o tempo passa."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/time.html#TimeSensor
        # Os nós TimeSensor podem ser usados para muitas finalidades, incluindo:
        # Condução de simulações e animações contínuas; Controlar atividades periódicas;
        # iniciar eventos de ocorrência única, como um despertador;
        # Se, no final de um ciclo, o valor do loop for FALSE, a execução é encerrada.
        # Por outro lado, se o loop for TRUE no final de um ciclo, um nó dependente do
        # tempo continua a execução no próximo ciclo. O ciclo de um nó TimeSensor dura
        # cycleInterval segundos. O valor de cycleInterval deve ser maior que zero.

        # Deve retornar a fração de tempo passada em fraction_changed

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("TimeSensor : cycleInterval = {0}".format(cycleInterval)) # imprime no terminal
        print("TimeSensor : loop = {0}".format(loop))

        # Esse método já está implementado para os alunos como exemplo
        epoch = time.time()  # time in seconds since the epoch as a floating point number.
        fraction_changed = (epoch % cycleInterval) / cycleInterval

        return fraction_changed

    @staticmethod
    def splinePositionInterpolator(set_fraction, key, keyValue, closed):
        """Interpola não linearmente entre uma lista de vetores 3D."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/interpolators.html#SplinePositionInterpolator
        # Interpola não linearmente entre uma lista de vetores 3D. O campo keyValue possui
        # uma lista com os valores a serem interpolados, key possui uma lista respectiva de chaves
        # dos valores em keyValue, a fração a ser interpolada vem de set_fraction que varia de
        # zeroa a um. O campo keyValue deve conter exatamente tantos vetores 3D quanto os
        # quadros-chave no key. O campo closed especifica se o interpolador deve tratar a malha
        # como fechada, com uma transições da última chave para a primeira chave. Se os keyValues
        # na primeira e na última chave não forem idênticos, o campo closed será ignorado.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("SplinePositionInterpolator : set_fraction = {0}".format(set_fraction))
        print("SplinePositionInterpolator : key = {0}".format(key)) # imprime no terminal
        print("SplinePositionInterpolator : keyValue = {0}".format(keyValue))
        print("SplinePositionInterpolator : closed = {0}".format(closed))

        # Abaixo está só um exemplo de como os dados podem ser calculados e transferidos
        value_changed = [0.0, 0.0, 0.0]
        
        return value_changed

    @staticmethod
    def orientationInterpolator(set_fraction, key, keyValue):
        """Interpola entre uma lista de valores de rotação especificos."""
        # https://www.web3d.org/specifications/X3Dv4/ISO-IEC19775-1v4-IS/Part01/components/interpolators.html#OrientationInterpolator
        # Interpola rotações são absolutas no espaço do objeto e, portanto, não são cumulativas.
        # Uma orientação representa a posição final de um objeto após a aplicação de uma rotação.
        # Um OrientationInterpolator interpola entre duas orientações calculando o caminho mais
        # curto na esfera unitária entre as duas orientações. A interpolação é linear em
        # comprimento de arco ao longo deste caminho. Os resultados são indefinidos se as duas
        # orientações forem diagonalmente opostas. O campo keyValue possui uma lista com os
        # valores a serem interpolados, key possui uma lista respectiva de chaves
        # dos valores em keyValue, a fração a ser interpolada vem de set_fraction que varia de
        # zeroa a um. O campo keyValue deve conter exatamente tantas rotações 3D quanto os
        # quadros-chave no key.

        # O print abaixo é só para vocês verificarem o funcionamento, DEVE SER REMOVIDO.
        print("OrientationInterpolator : set_fraction = {0}".format(set_fraction))
        print("OrientationInterpolator : key = {0}".format(key)) # imprime no terminal
        print("OrientationInterpolator : keyValue = {0}".format(keyValue))

        # Abaixo está só um exemplo de como os dados podem ser calculados e transferidos
        value_changed = [0, 0, 1, 0]

        return value_changed

    # Para o futuro (Não para versão atual do projeto.)
    def vertex_shader(self, shader):
        """Para no futuro implementar um vertex shader."""

    def fragment_shader(self, shader):
        """Para no futuro implementar um fragment shader."""

from viktor import ViktorController
from viktor.views import PlotlyView, PlotlyResult
from viktor import ViktorController
from viktor.parametrization import ViktorParametrization, TextField, NumberField, OptionField, LineBreak, Tab, Section, DownloadButton, Text
from viktor.views import GeometryView, GeometryResult, DataView, DataResult, DataGroup, DataItem, PlotlyView, PlotlyResult, WebResult, WebView
from viktor.result import DownloadResult
import topologicpy
from topologicpy.Vertex import Vertex
from topologicpy.Wire import Wire
from topologicpy.Face import Face
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Topology import Topology
from topologicpy.Graph import Graph
from topologicpy.Plotly import Plotly
from topologicpy.Cell import Cell
from topologicpy.Helper import Helper
# from topologicpy.Honeybee import Honeybee as HB
from topologicpy.Edge import Edge
from topologicpy.Dictionary import Dictionary
import plotly


class Parametrization(ViktorParametrization) :
    #Podium parameters


    tab_0 = Tab ("Introduction")
    tab_0.section_1 = Section("About")
    tab_0.section_1.text_1= Text(" The project involves using a Topologic Python library to create a tower within the VIKTOR app. The main objective of this project is to demonstrate the integration of the Topologic library with the VIKTOR app.\nThe integration of the Topologic library with the VIKTOR app enables users to explore and manipulate the tower's design and some features, allowing for a more interactive and dynamic architectural experience. This project aims to showcase the seamless integration of these two technologies, highlighting the potential for advanced geometric modeling and design analysis capabilities within the VIKTOR app.\n")
    tab_0.section_1.text_2 = Text(" Note: To run the app, please sequentially go through the tab, i.e., Podium > Internal Faces > External Faces > Adjacent Blocks > Building Graph")
    
    tab_0.section_2 = Section("More Info")
    tab_0.section_2.text_1  = Text("Tower tab visualise the complete tower design.")
    tab_0.section_2.text_2  = Text("Internal Faces tab displays the vertical internal faces, either of a particular floor or of a whole building.\n")
    tab_0.section_2.text_3 = Text("External Faces tab displays the External faces, either of a particular floor or of a whole building.\n")
    tab_0.section_2.text_4 = Text("Adjacent Block tab give an adjacent blocks of a selected block.\n")
    tab_0.section_2.text_5 = Text("Building Graph create a graph of a designed building.\n")


    tab_1 = Tab("Tower parameters")

    tab_1.section_1 = Section("Podium Parameters")
    tab_1.section_1.podL = NumberField( "Podium Length", default= 30, step= 2, suffix= "m")
    tab_1.section_1.podW = NumberField("Podium Width", default= 40, step= 2, suffix= "m")
    tab_1.section_1.podWsplit = NumberField("Podium Width Split", default= 3, step= 1, suffix= "m", variant="slider", min=1, max=6)
    tab_1.section_1.podLsplit = NumberField("Podium Length Split", default= 3, step= 1, suffix= "m", variant="slider", min=1, max=6)
    tab_1.section_1.podFlrHt = NumberField("Podium Floor Ht", default= 4, step= 1, suffix= "m",  variant="slider", min=4, max=6)
    tab_1.section_1.PodNoOfFlr = NumberField("No. of Podium Flrs", default= 2, step= 1, suffix= "m", variant="slider", min=1, max=4)
    tab_1.section_1.coreL = NumberField("Core Length", default= 6, step= 1, suffix= "m", min=2, max=8)
    tab_1.section_1.coreW = NumberField("Core Width", default= 6, step= 1, suffix= "m", min=2, max=8)
    tab_1.section_1.PodscaleF = NumberField("Pod Window Size", default= 0.4, step= 0.1, suffix= "m", variant="slider", min=0.4, max=0.8)
   
    
    tab_1.section_2 = Section("Building Parameters")
    tab_1.section_2.bldgWsplit = NumberField("Building Width Split", default= 3, step= 1, suffix= "m",  variant="slider", min=1, max=6)
    tab_1.section_2.bldgLsplit = NumberField("Building Length Split", default= 3, step= 1, suffix= "m",  variant="slider", min=1, max=6)
    tab_1.section_2.bldgFlrHt = NumberField("Building Floor Ht", default= 3, step= 1, suffix= "m", variant="slider", min=3, max=4)
    tab_1.section_2.bldgNoOfFlr = NumberField("No. of Building Flrs", default= 4, step= 1, suffix= "m", variant="slider", min=1, max=12)
    tab_1.section_2.bldgScaleF = NumberField(" Bldg Window Size", default= 0.5, step= 0.1, suffix= "m", variant="slider", min=0.5, max=0.8)
    
    tab_1.section_3 = Section("Tower Design Features")
    tab_1.section_3.xJagBool = OptionField("Jaggered Bldg in X-Axis", options = ["True", "False"], default = "False")
    tab_1.section_3.yJagBool = OptionField("Jaggered Bldg in Y-Axis", options = ["True", "False"], default = "False")
    tab_1.section_3.jagV = NumberField("Jaggered Value", default= 0, step= 1, suffix= "m", variant="slider", min=0, max=5)
    tab_1.section_3.scaleF = OptionField("Scale building", options = ["True", "False"], default = "False")
    tab_1.section_3.scaleV = NumberField("Scale Alternate Floors", default= 0.6, step= 0.1, suffix= "m", variant="slider", min=0.5, max=0.9)
    tab_1.section_3.rotateV = NumberField("Building Rotation", default= 0, step= 2.5, suffix= "m", variant="slider", min=0, max=15)
    
    tab_2 = Tab("Topologic Feature")
    tab_2.PodFloorNo = NumberField("Podium Floor", default= 1, step= 1, suffix= "m", min=0, max=100, description= "Internal vertical and external faces of a particular podium floor")
    tab_2.bldgFloorNo = NumberField("Building Floor", default= 1, step= 1, suffix= "m", min=0, max=100, description= "Internal vertical and external faces of a particular building floor")
    tab_2.cellCheck =  NumberField("Tower Cell", default= 1, step= 1, suffix= "m", min=0, max=100, description= "Select cell to check its adjacent topology")
    tab_2.IntParFace = OptionField("Particular Internal Floor", options = ["True", "False"], default = "True")
    tab_2.extParFace = OptionField("Particular External Floor", options = ["True", "False"], default = "True")
    # new_line = LineBreak()
    # tab_2.download_btn = DownloadButton("Download Honey-Bee file", "hbModel_download", longpoll=True)

class ModelController(ViktorController):    
    label = "Topologic Tower"
    parametrization = Parametrization   
    
    # aperCluFlrs  = [] # empty list to collect floor wise window aperture cluster
    # compPodFlrs  = [] # empty list to add floors with aperture
    # cluBldgWin  = [] # empty list to collect cluster window
    # compBldgFlrs  = []  # empty list to collect floors
    # winBldgWire  = [] # empty list to collect apertures wire
    # twrCells  = None
    # twrCellComplex  = None
    # twrWireframeGeo  = None
    # int_Faces  = []
    # hbModel  = None

    
    # def __init__(self ): 
    #     print('inside constructor')
    #     self.initialization()
    
    # # to prep-process and create objects
    # def initialization(self):
    #     print('print params.tab_1.section_1.PodNoOfFlr')
 
    @PlotlyView("Tower", duration_guess = 800) 
    def createPodium1(self, params, **kwargs ):
        # input parameters
        #Tab 1

        podL = params.tab_1.section_1.podL
        podW = params.tab_1.section_1.podW
        podWsplit = params.tab_1.section_1.podWsplit
        podLsplit = params.tab_1.section_1.podLsplit
        podFlrHt = params.tab_1.section_1.podFlrHt
        PodNoOfFlr = params.tab_1.section_1.PodNoOfFlr
        coreL = params.tab_1.section_1.coreL
        coreW = params.tab_1.section_1.coreW
        PodscaleF = params.tab_1.section_1.PodscaleF
        #Tab 2
        bldgL = params.tab_1.section_1.podL/2          # BuildingLength
        bldgW = params.tab_1.section_1.podW/3      # BuildingWidth
        bldgWsplit = params.tab_1.section_2.bldgWsplit
        bldgLsplit = params.tab_1.section_2.bldgLsplit
        bldgFlrHt = params.tab_1.section_2.bldgFlrHt
        bldgNoOfFlr = params.tab_1.section_2.bldgNoOfFlr
        bldgScaleF = params.tab_1.section_2.bldgScaleF
        #Tab 3
        # Section 1 - Building design parameters
        xJagBool = params.tab_1.section_3.xJagBool
        yJagBool = params.tab_1.section_3.yJagBool
        jagV = params.tab_1.section_3.jagV
        scaleF = params.tab_1.section_3.scaleF
        scaleV = params.tab_1.section_3.scaleV
        rotateV = params.tab_1.section_3.rotateV
        # Section 2 - Topologic Feature
        PodFloorNo = params.tab_2.PodFloorNo
        bldgFloorNo = params.tab_2.bldgFloorNo
        cellCheck = params.tab_2.cellCheck
        IntParFace = params.tab_2.IntParFace
        extParFace = params.tab_2.extParFace
         

        """ Create podium """ 
        # create single floor
        sinPodFlr = CellComplex.Box(width=podW, length=podL, height=4, 
                                    uSides=podWsplit, vSides=podLsplit, wSides=1, placement = 'bottom')

        # Decomposing the model
        DecPodDict = CellComplex.Decompose(sinPodFlr)
        PodExtVerFaces = DecPodDict['externalVerticalFaces']            # extracting vertical external surfaces from Dictionary
        # PodTopHorFaces = DecPodDict['topHorizontalFaces']
        # PodBotHorFaces = DecPodDict['bottomHorizontalFaces']
        # PodIntVerFaces = DecPodDict['internalVerticalFaces']
        # PodIntHorFaces = DecPodDict['internalHorizontalFaces']

        #create window aperture
        extWindow = []                                                                                                # empty list to collect window aperture
        # Iterating through all external faces
        for eachExtFace in PodExtVerFaces:                                                         
            centre = Topology.Centroid(eachExtFace)                                                   #centre of each faces
            extWindow.append(Topology.Scale(eachExtFace, centre, 
                                            x = PodscaleF, y= PodscaleF, z=PodscaleF))                # scaling external faces
        # Cluster of windows
        cluPodAper = Cluster.ByFaces(extWindow)

        # create core
        CorePod = CellComplex.Box(width=coreW, length=coreL, height=PodNoOfFlr*podFlrHt, 
                                uSides=1, vSides=1, wSides=PodNoOfFlr, placement = 'bottom')
        # create corridor
        corePodCordr = CellComplex.Box(width=coreW+2, length=coreL+2, height=PodNoOfFlr*podFlrHt, 
                                uSides=1, vSides=1, wSides=PodNoOfFlr, placement = 'bottom')
        # subtract corridor solid by core solid 
        podCorridor = Topology.Boolean(corePodCordr, CorePod, operation = 'difference',
                                    tranDict=False, tolerance= 0.0001)
        # subtracting corridor solid from podium floor
        diffPodFlr = Topology.Boolean(sinPodFlr, corePodCordr, operation = 'difference',
                                    tranDict=False, tolerance= 0.0001)

        # create podium floors and aperture
        PodFlrs = []                # empty list to collect podium floors
        aperCluFlrs = []          # empty list to collect floor wise window aperture cluster
        # create floors and aperture as per given floor
        for eachFlr in range(PodNoOfFlr):
            #append podium floor
            PodFlrs.append(Topology.Translate(diffPodFlr, z = eachFlr*podFlrHt))
            #append cluster aperture floor
            aperCluFlrs.append(Topology.Translate(cluPodAper, z = eachFlr*podFlrHt))

        #converting CellComplex core to cells
        CorePodCells = CellComplex.Cells(CorePod)                        # core cells
        CordrPodCells = CellComplex.Cells(corePodCordr)             # corridor cella
        #merging Core cells and Corridor cells by floor
        mrgeCore = []                                                                        # empty list to collect merge core and corridor cell
        # iterating through core and corridor cell floor wise
        for i,j in zip(CorePodCells, CordrPodCells):
            # boolean merge operation
            mrgeCore.append(Topology.Boolean(i, j, operation = 'merge',
                                        tranDict=False, tolerance= 0.0001))
        # merging each core and floor
        comPodFlrs = []                                                                      # empty list to collect merge  whole core and floor
        for eachFlr,eachcore in zip(PodFlrs,mrgeCore):
            # boolean merge operation
            comPodFlrs.append(Topology.Boolean(eachFlr, eachcore, operation = 'merge',
                                        tranDict=False, tolerance= 0.0001))

        # Adding aperture to the each podium floors
        global compPodFlrs
        compPodFlrs = []                                                                  # empty list to add floors with aperture
        # iterating through each floor and cluster aperture
        for eachFlr, echAperClu in zip(comPodFlrs,aperCluFlrs):
            # adding apertures to each floor
            compPodFlrs.append(Topology.AddApertures(eachFlr, Cluster.FreeFaces(echAperClu)))
        # getting aperture
        flrPodApr = []                                                                          # empty list to collect apertures of each floor
        # iterating through each floor and cluster aperture
        for echFlr in compPodFlrs:
            flrPodApr.append(Topology.ApertureTopologies(echFlr))
        # getting aperture wire
        winPodWire = []                                                                       # empty list to collect apertures wire
        # iterating through each aperture
        for list in flrPodApr:
            for echWin in list:
                #extracting wire
                winPodWire.append(Face.Wire(echWin))

        # extracting cells of each building floor : list in list
        CellPod = []                                                                             # empty list to collect cell of each floor
        # iterating through each floor
        for eachFlr in compPodFlrs:
            #getting cells from cellcomplex
            CellPod.append(CellComplex.Cells(eachFlr))

        # Flattening the list of cell
        fCellPod= Helper.Flatten(CellPod)

        """ Create building """ 

        #create vertex for building base
        centrePodTop = Vertex.ByCoordinates(0,0,PodNoOfFlr*podFlrHt)
        # create building base floor
        sinBldgFlr = CellComplex.Box(centrePodTop, width=bldgW, length=bldgL, height=bldgFlrHt, 
                                                        uSides=bldgWsplit, vSides=bldgLsplit, wSides=1, placement = 'bottom')

        # Creating first floor
        bldgBaseFlr = sinBldgFlr
        bldgFrstFlr = (Topology.Translate(sinBldgFlr, z = bldgFlrHt))

        # create building core
        CoreBldg = CellComplex.Box(centrePodTop, width=coreW, length=coreL, height=bldgNoOfFlr*bldgFlrHt,
                                                    uSides=1, vSides=1, wSides=bldgNoOfFlr, placement = 'bottom')

        #creating building corridor
        coreBldgCordr = CellComplex.Box(centrePodTop, width=coreW+2, length=coreL+2, height=bldgNoOfFlr*bldgFlrHt, 
                                uSides=1, vSides=1, wSides=bldgNoOfFlr, placement = 'bottom')

        # parameters
        # xJagBool = False        #Boolean to activate/deactivate jaggered building in X axis
        # yJagBool = False        #Boolean to activate/deactivate jaggered building in Y axis
        # jagV = 2                    # jaggered value for both direction
        # scaleF = True              #Boolean to activate/deactivate scale alternate floor
        # scaleV = .8                 # scale value to scale alternate floor

        xJagBool = xJagBool        #Boolean to activate/deactivate jaggered building in X axis
        yJagBool = yJagBool        #Boolean to activate/deactivate jaggered building in Y axis
        scaleF = scaleF              #Boolean to activate/deactivate scale alternate floor

        # creating building floors
        # if Scale is True
        if scaleF== "True":
            BldgFlrs = []                                                  # empty list to collect building floors
            # iterating
            for eachFlr in range(bldgNoOfFlr-1):
                # condition : both side jaggered
                if xJagBool == "True"  and  yJagBool == "True":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        Flr = Topology.Translate(bldgFrstFlr, x = move, y = move, z = eachFlr*bldgFlrHt)
                        BldgFlrs.append(Topology.Scale(Flr, Topology.Centroid(Flr), x=scaleV, y=scaleV))     
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, x = move, y = move, z = eachFlr*bldgFlrHt))
                # condition : no jaggered        
                if xJagBool == "False" and  yJagBool == "False":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        Flr = Topology.Translate(bldgFrstFlr, z = eachFlr*bldgFlrHt)
                        BldgFlrs.append(Topology.Scale(Flr, Topology.Centroid(Flr), x=scaleV, y=scaleV))
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, z = eachFlr*bldgFlrHt))
                # condition: only x axis jaggered    
                if xJagBool == "True"  and yJagBool  == "False":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        Flr = Topology.Translate(bldgFrstFlr, x = move, z = eachFlr*bldgFlrHt)
                        BldgFlrs.append(Topology.Scale(Flr, Topology.Centroid(Flr), x=scaleV, y=scaleV))
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, x = move, z = eachFlr*bldgFlrHt))
                # condition: y asix jaggered    
                if xJagBool  == "False" and  yJagBool == "True":
                        # condition to segregate alternate floor
                        if eachFlr % 2 == 0:
                            move = jagV                                     # jaggered value
                            BldgFlrs.append(Topology.Translate(bldgFrstFlr, y = move, z = eachFlr*bldgFlrHt))
                        else:
                            move = -(jagV)                                  # negative jaggered value
                            BldgFlrs.append(Topology.Translate(bldgFrstFlr, y = move, z = eachFlr*bldgFlrHt))
        # if Scale is False
        else:
            BldgFlrs = []                                                  # empty list to collect building floors
            for eachFlr in range(bldgNoOfFlr-1):
                # both side jaggered
                if xJagBool == "True"  and  yJagBool  == "True":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, x = move, y = move, z = eachFlr*bldgFlrHt))
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, x = move, y = move, z = eachFlr*bldgFlrHt))
                # condition : no jaggered    
                if xJagBool == "False" and yJagBool  == "False":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, z = eachFlr*bldgFlrHt))
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, z = eachFlr*bldgFlrHt))
                # condition: only x axis jaggered    
                if xJagBool == "True" and yJagBool  == "False":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, x = move, z = eachFlr*bldgFlrHt))
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, x = move, z = eachFlr*bldgFlrHt))
                # condition: y asix jaggered   
                if xJagBool  == "False" and  yJagBool  == "True":
                    # condition to segregate alternate floor
                    if eachFlr % 2 == 0:
                        move = jagV                                     # jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, y = move, z = eachFlr*bldgFlrHt))
                    else:
                        move = -(jagV)                                  # negative jaggered value
                        BldgFlrs.append(Topology.Translate(bldgFrstFlr, y = move, z = eachFlr*bldgFlrHt))

        # combining Ground Floor and upper floors
        BldgFlrs.insert(0, bldgBaseFlr)

        # adding rotation to each floor
        AllFlrs = []        # empty list to collect floors
        i = 0
        while i < len(BldgFlrs): 
            for flr in BldgFlrs:
                i+=1
                #adding rotation
                AllFlrs.append(Topology.Rotate(flr, Topology.Centroid(flr), degree= i*rotateV))

        # subtract corridor solid by core solid 
        bldgCorridor = Topology.Boolean(coreBldgCordr, CoreBldg, operation = 'difference',
                                    tranDict=False, tolerance= 0.0001)
        # Subtracting core from podium floor
        diffBldgFlr = []   # emtpy list
        # iterating through all floors
        for eachFlr in AllFlrs:
            # boolean difference operation
            diffBldgFlr.append(Topology.Boolean(eachFlr, coreBldgCordr, operation = 'difference',
                                    tranDict=False, tolerance= 0.0001))

        #converting CellComplex core to cells
        CoreCells = CellComplex.Cells(CoreBldg)
        CordrBldgCells = CellComplex.Cells(bldgCorridor)
        # merging each core cell  and corridor cell by floor
        mrgeCore = []                  # emtpy list  
        for i,j in zip(CoreCells, CordrBldgCells):
            # boolean merge operation
            mrgeCore.append(Topology.Boolean(i, j, operation = 'merge',
                                        tranDict=False, tolerance= 0.0001))
        # merging each core and each floors
        comBldgFlrs = []                               # emtpy list
        for eachFlr,eachcore in zip(diffBldgFlr,mrgeCore):
            # boolean merge operation
            comBldgFlrs.append(Topology.Boolean(eachFlr, eachcore, operation = 'merge',
                                        tranDict=False, tolerance= 0.0001))

        # Decomposing the model
        BldgExtVerFaces = []        # empty list to collect external vertical faces
        extBldgWindow = []        # empty list to collect window
        # iterating through all floors
        for echFlr in AllFlrs:
            # decompose each floors
            DecBldgDict = CellComplex.Decompose(echFlr)
            # extracting vertical external surfaces from Dictionary
            BldgExtVerFaces.append(DecBldgDict['externalVerticalFaces'])
        # iterating through all external vertical faces
        for echExtFaceList in BldgExtVerFaces:
            for i in echExtFaceList:
                # scaling object
                extBldgWindow.append(Topology.Scale(i, Topology.Centroid(i), 
                                    x = bldgScaleF, y= bldgScaleF, z=bldgScaleF))
        # create list in list : data management
        windw = []
        # creating list in list
        for i in range(0, len(extBldgWindow), len(BldgExtVerFaces[0])):
            windw.append(extBldgWindow[i:i + len(BldgExtVerFaces[0])])

        # create cluster of each floors windows
        cluBldgWin = []             # empty list to collect cluster window
        # iterating through list of windows
        for list in windw:
                # create cluster
                cluBldgWin.append(Cluster.ByTopologies(list))

        # Adding aperture to the each podium floors
        global compBldgFlrs
        compBldgFlrs =[]                                   # empty list to collect floors
        # iterating through each floor and window cluster
        for echFlr, echBldgAprClu in zip(comBldgFlrs, cluBldgWin):
            # adding aperture
            compBldgFlrs.append(Topology.AddApertures(echFlr, Cluster.FreeFaces(echBldgAprClu)))
        # getting aperture
        flrBldgApr = []                                    # empty list to collect windows aperture
        # iterating through each floors
        for echFlr in compBldgFlrs:
            # get aperture topology
            flrBldgApr.append(Topology.ApertureTopologies(echFlr))
        # getting aperture wire
        winBldgWire = []                                # empty list to collect apertures wire
        for list in flrBldgApr:
            for echWin in list:
                #extracting wire
                winBldgWire.append(Face.Wire(echWin))

        # extracting cells of each building floor : list in list
        CellBldg = []                                       # empty list to collect cell of each floor
        # iterating through each floor
        for eachFlr in compBldgFlrs:
            #getting cells from cellcomplex
            CellBldg.append(CellComplex.Cells(eachFlr))

        # Flattening the list of cell
        fCellBldg = Helper.Flatten(CellBldg)

        # merge all cells list
        global twrCells
        twrCells = fCellPod + fCellBldg
        # merge aperture wire
        twrAprWire = winPodWire + winBldgWire
        # merge aperture face
        twrAprFace = flrPodApr + extBldgWindow
        # merge all cellComplex list
        global twrCellComplex
        twrCellComplex = compPodFlrs + compBldgFlrs

        """ vvv --- whole tower visualisation --- vvv """

        podGeo = Plotly.DataByTopology(Cluster.ByTopologies(fCellPod), faceLegendLabel = "Podium", 
                                    faceColor='rgba(255, 255, 255, 0.8)')
        bldgGeo = Plotly.DataByTopology(Cluster.ByTopologies(fCellBldg), faceLegendLabel = "Tower", 
                                    faceColor='rgba(255, 255, 255, 0.8)')

        aprFaceGeo = Plotly.DataByTopology(Cluster.ByTopologies(Helper.Flatten(twrAprFace)), faceLegendLabel= "Aperture" , faceColor='rgba(198, 244, 248, 0.8)')
        twrPlotFig = Plotly.FigureByData(podGeo + bldgGeo + aprFaceGeo)
        return PlotlyResult(twrPlotFig.to_json())
    


    @PlotlyView("Internal Faces", duration_guess = 800) 
    def InteriorWalls(self, params, **kwargs ):
        PodNoOfFlr = params.tab_1.section_1.PodNoOfFlr
        bldgNoOfFlr = params.tab_1.section_2.bldgNoOfFlr
        # To check internal vertical and external faces of a particular podium and building floor
        PodFloorNo = params.tab_2.PodFloorNo           # select floor to visualise internal vertical and external faces
        bldgFloorNo = params.tab_2.bldgFloorNo         # select floor to visualise internal vertical and external faces
        #type "None" to deactivate podium or buiding floor

        intPodFaces = []          # empty list to collect vertical internal podium faces
        extPodFaces =[]          # empty list to collect external podium faces
        intBldgFaces = []         # empty list to collect vertical internal building faces
        extBldgFaces = []        # empty list to collect external building faces

        #check the input of floor no of building and podium
        # if only podium floor is given
        if PodFloorNo is not None and bldgFloorNo is None: 
            # to check if floor no is valid
            if PodFloorNo <= PodNoOfFlr - 1:
                #iterating through each cellcomplex(floors) and extracting internal faces
                for echFace in CellComplex.InternalFaces(compPodFlrs[PodFloorNo]):
                    intPodFaces.append(echFace)
                #iterating through each cellcomplex(floors) and extracting external faces
                for echFace in CellComplex.ExternalFaces(compPodFlrs[PodFloorNo]):
                    extPodFaces.append(echFace)
            # if not a valid floor no: throw error
            else:
                print("Value should be within No, of floors. i.e 0 to", PodNoOfFlr - 1)
        #if both floors no is given
        elif PodFloorNo and bldgFloorNo is not None:
            if PodFloorNo <= PodNoOfFlr - 1 and bldgFloorNo <= bldgNoOfFlr-1:
                #iterating through each cellcomplex(floors) and extracting internal faces
                for echFace in CellComplex.InternalFaces(compPodFlrs[PodFloorNo]):  
                    intPodFaces.append(echFace)
                #iterating through each cellcomplex(floors) and extracting external faces
                for echFace in CellComplex.ExternalFaces(compPodFlrs[PodFloorNo]):
                    extPodFaces.append(echFace)
                #iterating through each cellcomplex(floors) and extracting internal faces
                for echFace in CellComplex.InternalFaces(compBldgFlrs[bldgFloorNo]):  
                    intBldgFaces.append(echFace)
                #iterating through each cellcomplex(floors) and extracting external faces
                for echFace in CellComplex.ExternalFaces(compBldgFlrs[bldgFloorNo]):
                    extBldgFaces.append(echFace)
            # if not a valid floor no: throw error
            else:
                print("Value should be within No, of floors. i.e for Podium: 0 to", PodNoOfFlr - 1, "\nValue should be within No, of floors. i.e for Building: 0 to", bldgNoOfFlr - 1)
        # if only building floor is given
        elif PodFloorNo is None and bldgFloorNo is not None :
            if bldgFloorNo <= bldgNoOfFlr-1:
                #iterating through each cellcomplex(floors) and extracting internal faces
                for echFace in CellComplex.InternalFaces(compBldgFlrs[bldgFloorNo]):  
                    intBldgFaces.append(echFace)
                #iterating through each cellcomplex(floors) and extracting external faces
                for echFace in CellComplex.ExternalFaces(compBldgFlrs[bldgFloorNo]):
                    extBldgFaces.append(echFace)
            # if not a valid floor no: throw error
            else:
                print("Value should be within No, of floors. i.e  0 to", bldgNoOfFlr - 1)
        else:
            # if not a valid floor no: throw error
            pass
            print("Please enter value of podium or building floor to get internal and external faces.")


        """ vvv --- whole tower internal and external faces --- vvv """

        # getting whole tower internal and external faces
        intAllFaces = []                        # empty list to collect all vertical internal faces
        extAllFaces = []                        # empty list to collect all external faces

        # iterating through all cellcomplex(floors) and extracting all internal and external faces
        for echflr in twrCellComplex:
            # appending internal and external faces of each cellcomplex(floor)
            intAllFaces.append(CellComplex.InternalFaces(echflr))
            extAllFaces.append(CellComplex.ExternalFaces(echflr))

        # Flattening the list of cell
        fIntAllFaces = Helper.Flatten(intAllFaces)              # flatten list
        fExtAllFaces = Helper.Flatten(extAllFaces)             # flatten list
        # create building wire
        twrTopoWires = Topology.SubTopologies(CellComplex.ByCells(twrCells), subTopologyType= "wire")
        "-------------------------------------------------------------------------------------------------"
        global twrWireframeGeo
        twrWireframeGeo = Plotly.DataByTopology(Cluster.ByTopologies(twrTopoWires), edgeLabelKey= "Tower wireframe" , edgeColor='rgba(8, 14, 44, .5)',edgeWidth=1)

        # visualisation of whole tower internal and external faces
        allIntFaceGeo = Plotly.DataByTopology(Cluster.ByTopologies(fIntAllFaces), faceLegendLabel = "Internal Faces", 
                                    faceColor='rgba(196, 77, 86, .5)')                                                                                                 # All internal faces
        allExtFaceGeo = Plotly.DataByTopology(Cluster.ByTopologies(fExtAllFaces), faceLegendLabel = "External Faces", 
                                    faceColor='rgba(255, 252, 127, 1)')                                                                                            # All external faces
        # plot by figure
        allIntFacePlotFig = Plotly.FigureByData(allIntFaceGeo + twrWireframeGeo)
        allIExtFacePlotFig = Plotly.FigureByData(allExtFaceGeo+ twrWireframeGeo)
        allFacePlotFig = Plotly.FigureByData(allIntFaceGeo + allExtFaceGeo)

        """ ^^^ --- whole tower internal and external faces --- ^^^ """


        """ vvv --- individual tower floor internal and external faces --- vvv """

        # merge list    
        indIntVerFace = intPodFaces + intBldgFaces                      # merge internal faces of building and podium 
        indExttVerFace = extPodFaces + extBldgFaces                   # merge external faces of building and podium 
        # visualisation ofselected floor internal and external faces
        indIntFaceGeo = Plotly.DataByTopology(Cluster.ByTopologies(indIntVerFace), faceLegendLabel = "Internal Faces", 
                                    faceColor='rgba(196, 77, 86, .5)')                                                                                                 # selected floor internal faces
        intExtFaceGeo = Plotly.DataByTopology(Cluster.ByTopologies(indExttVerFace), faceLegendLabel = "External Faces", 
                                    faceColor='rgba(255, 252, 127, 1)')                                                                                              # selected floor external faces
        # plot by figure
        indIntFacePlotFig = Plotly.FigureByData(indIntFaceGeo + twrWireframeGeo)
        indExtFacePlotFig = Plotly.FigureByData(intExtFaceGeo+ twrWireframeGeo)
        indFacePlotFig = Plotly.FigureByData(indIntFaceGeo + intExtFaceGeo + twrWireframeGeo)
    
        
        "-------------------------------------------------------------------------------------------------"
        int_Faces = [allIntFacePlotFig, indIntFacePlotFig]
        global ext_Faces
        ext_Faces = [allIExtFacePlotFig, indExtFacePlotFig]
        
        IntParFace = params.tab_2.IntParFace

        if IntParFace == "True":
            return(PlotlyResult(int_Faces[1].to_json()))
        
        else: 
            return(PlotlyResult(int_Faces[0].to_json()))


    @PlotlyView("External Faces", duration_guess =  800) 
    def Internal_faces(self, params, **kwargs ):
        extParFace = params.tab_2.extParFace       
        if extParFace == "True":
            return(PlotlyResult(ext_Faces[1].to_json()))
        
        else: 
            return(PlotlyResult(ext_Faces[0].to_json()))


    @PlotlyView("Adjacent Blocks", duration_guess = 600) 
    def Adjacent_block(self, params, **kwargs ):

        #select cell to check its adjacent topology
        cellCheck = params.tab_2.cellCheck

        # check if given value is valid
        if cellCheck <= len(twrCells)-1:
            #create cellcomplex
            twrCC = CellComplex.ByCells(twrCells)
            # getting cells from cellcomplex
            twrTopoCells = Topology.SubTopologies(twrCC, "cell")
            #cell to get adjacent topology of
            srchItem = twrTopoCells[cellCheck]
            #getting adjacent topology
            AdjCells = Topology.AdjacentTopologies(srchItem, twrCC)
        else:
            # if not a valid : throw error and suggest
            print("Please enter cell value between 0 to len(twrCells)-1")

        # visualision for adjacent blocks

        geo1 = Plotly.DataByTopology(srchItem, faceLegendLabel = "Cell to find adjacent topology", 
                                    faceColor='rgba(196, 77, 86, 1)')                                                                  #Cell to find adjacent topology
        geo2 = Plotly.DataByTopology(Cluster.ByTopologies(AdjCells), faceLegendLabel = "Adjacent cell of selected topology",
                                    faceColor='rgba(255, 252, 127, .7)')                                                            #Adjacent cell of selected topology
        twrGeoFade = Plotly.DataByTopology(Cluster.ByTopologies(twrCells), faceLegendLabel = "Tower", edgeWidth=.5, edgeColor= 'rgba(100, 100, 100, 1)', vertexColor= 'rgba(100, 100, 100, 0.1)', 
                              faceColor='rgba(255, 255, 255, .2)')
        
        plotfig1 = Plotly.FigureByData(geo1 + geo2 + twrGeoFade + twrWireframeGeo)                                         # plot by figure                                                                   # plot data
        return PlotlyResult(plotfig1.to_json())


    @PlotlyView("Building Graph", duration_guess = 200) 
    def Building_Graph(self, params, **kwargs ):
        # create graph

        twrGraph = Graph.ByTopology(Cluster.ByTopologies(twrCells), direct=True, directApertures=False, viaSharedTopologies=True,
                                    viaSharedApertures=False, toExteriorTopologies=True, toExteriorApertures=False,
                                    toContents=False, useInternalVertex=True, storeBRep=True, tolerance=0.0001)

        twrGraphGeo = Plotly.DataByGraph(twrGraph, vertexColor='black', vertexSize=2, vertexLabelKey=None, vertexGroupKey=None, vertexGroups=[], showVertices=True, edgeColor='black', edgeWidth=2, edgeLabelKey=None, edgeGroupKey=None, edgeGroups=[], showEdges=True)
        twrGeoFade = Plotly.DataByTopology(Cluster.ByTopologies(twrCells), faceLegendLabel= "Tower", edgeWidth=.5, edgeColor= 'rgba(100, 100, 100, 1)', vertexColor= 'rgba(100, 100, 100, 0.1)', 
                                    faceColor='rgba(255, 255, 255, .3)')

        plotfig1 = Plotly.FigureByData(twrGraphGeo + twrGeoFade)                                         # plot by figure
        # Plotly.Show(plotfig1, renderer = 'notebook')
        return PlotlyResult(plotfig1.to_json())
        
    # @PlotlyView("HoneyBee Model", duration_guess = 800) 
    # def HoneyBee_Model(self, params, **kwargs ):
        # Honeybee Code

        # # shading
        # # getting edges of windows
        # edgs = []
        # for i in self.winBldgWire:
        #     # for echwire in i:
        #     edgs.append(Wire.Edges(i))

        # topEdges = []
        # for list in edgs:
        #     topEdges.append(list[2])
        # off = []
        # for i in topEdges:
        #     offset = Edge.ByOffset2D(i, 1)
        #     off.append(Edge.Reverse(offset))
        # vert = []                  # empty list to store top window edge
        # shade = []              # empty list to store shade(face)
        # for i, j in zip(topEdges, off):
        #     vert.append((Edge.Vertices(i)) + (Edge.Vertices(j)) )
        # for vertlist in vert:
        #     shade.append(Face.ByVertices(vertlist))

        # clu = Cluster.ByTopologies(self.twrCells)                    # cluster of building cells

        # allApr = self.aperCluFlrs + self.cluBldgWin                       # merge all wnaperture cluster
        # aprClu = Cluster.ByTopologies(allApr)                  # cluster of windows
        # aperture = Topology.SubTopologies(aprClu, subTopologyType='face')    # extract face from clusters
        # d = Dictionary.ByKeysValues(["type"], ["window"])
        # compApr = []
        # for i in aperture:
        #     compApr.append(Topology.SetDictionary(i,d))
            
        # # mergeall
        # mrgAll = Topology.MergeAll(self.twrCells)

        # model = Topology.AddApertures(clu, compApr, exclusive=True, subTopologyType= 'face', tolerance= 0.0001)                                        #add aperture to model(cluster)

        # #  subTopologyType="face"
        # getApr = Topology.ApertureTopologies(model, subTopologyType= 'face')                                        # extracting apertures from model

        # # create hb model
        # self.hbModel = HB.ModelByTopology(model, tpShadingFacesCluster=Cluster.ByTopologies(shade))

        # # visualisation
        # twrGeo = Plotly.DataByTopology(model, faceLegendLabel = "Tower", faceColor='rgba(225, 225, 225, .8)')     
        # aperGeo = Plotly.DataByTopology(Cluster.ByTopologies(aperture), faceLegendLabel = "Aperture", faceColor='rgba(196, 77, 86, 1)')
        # shadeGeo = Plotly.DataByTopology(Cluster.ByTopologies(shade), faceLegendLabel = "Shade", faceColor='rgba(62, 28, 255 1)')
        # twrPlotFig = Plotly.FigureByData(twrGeo + aperGeo + shadeGeo)
        # return(PlotlyResult(twrPlotFig.to_json()))


    # def test(self, params, **kwargs ):
    #     print("print Params, Def without visualisation")
    #     print(params.bldgNoOfFlr)

    # def hbModel_download(self, params, **kwargs):
    #     return DownloadResult(file_content='self.hbModel', file_name='Topo_HB_Model.hbjson')
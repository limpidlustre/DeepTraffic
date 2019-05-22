class Config:
	def __init__(self):
		self.mode = 'train'

		self.nsteps_train = 100000
		self.print_freq = 50
		self.target_update_freq = 1000
		self.saving_freq = 25000
		self.simulation_freq = 1000
		self.model_output = '../output'

		self.eps_begin = 1.0
		self.eps_end = 0.1
		self.nsteps = 1000
		self.dropout= 0.9

		self.lr_begin = 0.00025
		self.lr_end = 0.00005
		self.lr_nsteps = self.nsteps_train / 2

		self.gamma = 0.99
		self.grad_clip = True
		self.clip_val = 10
		self.batch_size = 32

		self.T = 100
		self.N = 100
		self.nBufferSample = 100

		self.hidden_size= 10
		self.numActions = 5

		self.numCars = 20
		self.numLanes = 7
		self.canvasHeight = 700
		self.canvasWidth = 140
		self.gridHeight = 10
		self.carHeightGrid = 4
		self.decisionFreq = 5
		self.speedScaling = 15
		self.actionSpeedHistory = 5
		self.egoTopSpeed = 80.0
		self.carTopSpeed = 65.0
		self.acc = 0.01
		self.minSpeedFrac = 0.5
		self.egoCarPos = 18.0
		self.state_length = 1 + 2 + 2 * self.actionSpeedHistory + \
								self.numLanes * self.canvasHeight // self.gridHeight + \
								3 * self.numCars
		self.state_history = 1
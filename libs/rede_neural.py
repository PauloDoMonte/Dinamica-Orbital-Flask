def load_rna():
	import pickle


	with open('redes_neurais/rna.pkl', mode='rb') as f:
		rna = pickle.load(f)

	layers 				= rna.n_layers_
	loss 				= rna.loss_
	learning_rate 		= rna.learning_rate
	hidden_layer_sizes	= rna.hidden_layer_sizes
	coefs 				= rna.coefs_

	return(layers,loss,learning_rate,hidden_layer_sizes,coefs)
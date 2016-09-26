import numpy as np
class Structure:
	def __init__(self, k, wn, zeta):
		self.k = k;
		self.wn = wn*2*np.pi;
		self.zeta = zeta;
		self.m = k/(self.wn*self.wn);
		for i in range(np.size(k)):
			print i+1,' mode';
			print "k=",k[i]/1e6,"kN/mm";
			print "zeta=",zeta[i];
			print "wn=",wn[i],"Hz";
	def TF(self,w): #TransferFunction
		w = w*np.array([1j])
		k = self.k;
		wn= self.wn;
		zeta = self.zeta;
		m = self.m;
		#y = 1/m / (w*w + 2 * zeta * w * wn + wn^2);
		y = (1/m[0])/ (w*w + 2 * zeta[0] * w * wn[0] + wn[0]*wn[0]);
		for i in range(1,np.size(k)):
			y += (1/m[i]) / (w*w + 2 * zeta[i] * w * wn[i] + wn[i]*wn[i]);
		return y;


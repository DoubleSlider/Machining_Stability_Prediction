import numpy as np
pi = np.pi;
class Budak:
	def __init__(self, Kt, Kr,N):
		self.Kr = Kr;
		self.Kt = Kt;
		self.N = N;
	def Axx(self,th):
		return 0.5 * ( np.cos(2*th) - 2*self.Kr*th + self.Kr * np.sin(2*th) );
	def Axy(self,th):
		return 0.5 * (-np.sin(2*th) - 2*th + self.Kr * np.cos(2*th) );
	def Ayx(self,th):
		return 0.5 * (-np.sin(2*th) + 2*th + self.Kr * np.cos(2*th) );
	def Ayy(self,th):
		return 0.5 * (-np.cos(2*th) - 2*self.Kr*th - self.Kr * np.sin(2*th) );

	def Calc(self,Gxx, Gyy, Wc, phi_st, phi_ex):
		axx = self.Axx(phi_ex) - self.Axx(phi_st);
		axy = self.Axy(phi_ex) - self.Axy(phi_st);
		ayx = self.Ayx(phi_ex) - self.Ayx(phi_st);
		ayy = self.Ayy(phi_ex) - self.Ayy(phi_st);

		#A0 = axx * ayy - axy * ayx;
		#A0 = np.array(Gxx) * np.array(Gyy);
		A0 = Gxx * Gyy * (axx * ayy - axy * ayx);
		A1 = axx * Gxx + ayy * Gyy;
		Lambda = np.array([(-A1 + np.sqrt( A1*A1 - 4 * A0 ))/(2*A0),
						  (-A1 - np.sqrt( A1*A1 - 4 * A0 ))/(2*A0)]);

		Kappa = Lambda.imag/Lambda.real;
		a_lim = -2*pi*Lambda.real/self.N/self.Kt * (1+Kappa*Kappa);
		#a_lim = np.zeros(np.size(Gxx));
		ap =np.array([]);
		Lda =np.array([]);
		wc =np.array([]);
		kappa = np.array([]);

		for i in range(np.size(Gxx)):
			if (a_lim[0,i] > 0 and a_lim[1,i] < 0) or ( a_lim[1,i] > a_lim[0,i] and a_lim[0,i] > 0) :
				ap = np.append(ap, a_lim[0,i]);
				Lda = np.append(Lda, Lambda[0,i]);
				wc = np.append(wc,Wc[i]);
				kappa = np.append(kappa,Kappa[0,i]);
			elif (a_lim[1,i] > 0 and a_lim[0,i] < 0) or ( a_lim[0,i] > a_lim[1,i] and a_lim[1,i] > 0) :
				ap = np.append(ap, a_lim[1,i]);
				Lda = np.append(Lda, Lambda[1,i]);
				wc = np.append(wc,Wc[i]);
				kappa = np.append(kappa,Kappa[1,i]);

		return ap, kappa, wc


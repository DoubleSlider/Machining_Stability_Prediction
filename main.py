"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
import numpy as np
import matplotlib.pyplot as plt

import Structure as stct
import Budak as bdk




IsDownMill = False;
data_resolution = 2000;
pi=np.pi;
omega_cri = np.linspace(100,1000, data_resolution)*2*pi;




# eta_r mode
eta_r = 0.5;

if IsDownMill:
	phi_st = pi - np.arccos(1 - 2* eta_r); # entry_angle
	phi_ex = pi*np.ones(np.size(omega_cri)); # exit_angle
 #   Phi = [phi_st phi_ex];
else:
	phi_st = np.zeros(np.size(omega_cri));
	phi_ex = np.arccos(1 - 2*eta_r);
#    Phi = [phi_st phi_ex];

# set parameter
Kr = 0.3;
Kt = 2200e6;
N = 2;

Xk = np.array([2.26e8, 5.54e7]); # N/m
Yk = np.array([2.13e8, 2.14e7]); # N/m
Xwn = np.array([260, 389]); #Hz
Ywn = np.array([150, 348]); #Hz
Xzeta = np.array([0.12, 0.04]); # damping ratio
Yzeta = np.array([0.10, 0.10]); # ratio
Yk = Xk;
Ywn = Xwn;
Yzeta = Xzeta;

Gxx = stct.Structure( Xk, Xwn, Xzeta );
Gyy = stct.Structure( Yk, Ywn, Yzeta );
gxx=Gxx.TF( omega_cri );
gyy=Gxx.TF( omega_cri );

budak = bdk.Budak(Kt,Kr,N)
da_lim, Kappa, omega_cri = budak.Calc(gxx, gyy, omega_cri, phi_st, phi_ex);



print "wc size:", np.size(omega_cri)
print "da size:", np.size(da_lim)
print "kappa size:", np.size(Kappa)
wwww = np.arctan(1/Kappa);
for i in range(np.size(wwww)):
#	print i
#	print wwww[i]
	if wwww[i] < 0:
		wwww[i] += pi;
mode_number = 2
n = np.zeros((mode_number,np.size(omega_cri)))
for i in range(mode_number):
	T = (2*wwww + 2*i*pi)/omega_cri;
	n[i,:] = 60/N/T;
	#plot(n(i+1,:),da_lim,'k','linewidth',4)

#x = np.linspace(0, 10)
#line, = plt.plot(x, np.sin(x), '--', linewidth=2)
line, = plt.plot(n[0,:], da_lim, '-', linewidth=2)
plt.plot(n[1,:], da_lim, '-', linewidth=2)
#dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
#line.set_dashes(dashes)
fig2 = plt.figure()
plt.plot(omega_cri/2/pi, da_lim*1e3, '-', linewidth=2)
#plt.xlim(0, 1)
plt.ylim(0, 300)


fig3 = plt.figure()
plt.plot(gxx.real,gxx.imag)
fig4 = plt.figure()
plt.plot(gyy.real,gyy.imag)
plt.show()

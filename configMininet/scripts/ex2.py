from mininet.topo import Topo

class MyTopo (Topo):
	def __init__(self):
		Topo.__init__(self)
		
		serverhttp = self.addHost("serverhttp",ip='no ip defined/8')
		roteador = self.addHost("roteador",ip='no ip defined/8')
		
		r1h1 = self.addHost("r1h1", ip='no ip defined/8')
		r1h2 = self.addHost("r1h2", ip='no ip defined/8')
		r1h3 = self.addHost("r1h3", ip='no ip defined/8')

		r2h1 = self.addHost("r2h1", ip='no ip defined/8')
		r2h2 = self.addHost("r2h2", ip='no ip defined/8')
		r2h3 = self.addHost("r2h3", ip='no ip defined/8')

		s1 = self.addSwitch("s1")
		s2 = self.addSwitch("s2")

		self.addLink(serverhttp, s1)
		self.addLink(r1h1, s1)
		self.addLink(r1h2, s1)
		self.addLink(r1h3, s1)
		self.addLink(roteador, s1)

		self.addLink(r2h1, s2)
		self.addLink(r2h2, s2)
		self.addLink(r2h3, s2)
		self.addLink(roteador, s2)

topos = { 'mytopo': (lambda: MyTopo())}


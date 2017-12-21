from mininet.topo import Topo

class MyTopo(Topo):

	def __init__(self):
		Topo.__init__(self)
		
		serverdhcp = self.addHost("serverdhcp",ip='no ip defined/8')
		h1 = self.addHost("h1",ip='no ip defined/8')
		h2 = self.addHost("h2",ip='no ip defined/8')
		h3 = self.addHost("h3",ip='no ip defined/8')
		h4 = self.addHost("h4",ip='no ip defined/8')
		s1 = self.addSwitch("s1")

		self.addLink(serverdhcp,s1)
		self.addLink(h1,s1)
		self.addLink(h2,s1)
		self.addLink(h3,s1)
		self.addLink(h4,s1)

topos = {'mytopo': (lambda: MyTopo())}


===
FPO
===
FPO aims to be the be-all solution to your FPO'in image needs. You doing a project for PETA? God knows you don't want that delicious burger showing up in your comps by mistake. Does your company work exclusively with the government? Then of course everyone in that hot new responsive design should be in desert camo. FPO gives your organization complete control over your designers' image assets. 

Features
--------
- REST API for calling project or organization specific placement images resized to whatever size your project demands.
- Admin interface for interacting with projects and images specific to your organization.
- CLI interface for interacting with projects and images specific to your organization.

CLI Interface
-------------
::

fpo 1200x700 image1.jpg

fpo fit-height 1200x700 image1.jpg

fpo fit-box 1200x700 image1.jpg

fpo -o peta 1200x700 image1.jpg

fpo -n 10 1200x700 "image[\d].jpg"

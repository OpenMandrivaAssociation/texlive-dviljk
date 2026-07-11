%global tl_name dviljk
%global tl_revision 66186

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	DVI to Laserjet output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dviljk
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dviljk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dviljk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dviljk.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A dvi driver for the LaserJet printers, using kpathsea recursive file
searching. Note: this program will not compile simply with the sources
in this distribution; it needs a full (current) kpathsea distribution
environment, such as is available from the TeX Live source tree.


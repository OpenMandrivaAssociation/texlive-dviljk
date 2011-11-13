# revision 23089
# category TLCore
# catalog-ctan /dviware/dviljk
# catalog-date 2009-11-09 17:50:29 +0100
# catalog-license gpl
# catalog-version 2.6p4
Name:		texlive-dviljk
Version:	2.6p4
Release:	2
Summary:	DVI to Laserjet output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dviljk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviljk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviljk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dviljk.bin
%rename tetex-dvilj
%rename texlive-dvilj
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A dvi driver for the LaserJet printers, using kpathsea
recursive file searching. Note: this program will not compile
simply with the sources in this distribution; it needs a full
(current) kpathsea distribution environment, such as is
available from the TeX-Live source tree.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvihp.1*
%doc %{_texmfdir}/doc/man/man1/dvihp.man1.pdf
%doc %{_mandir}/man1/dvilj.1*
%doc %{_texmfdir}/doc/man/man1/dvilj.man1.pdf
%doc %{_mandir}/man1/dvilj2p.1*
%doc %{_texmfdir}/doc/man/man1/dvilj2p.man1.pdf
%doc %{_mandir}/man1/dvilj4.1*
%doc %{_texmfdir}/doc/man/man1/dvilj4.man1.pdf
%doc %{_mandir}/man1/dvilj4l.1*
%doc %{_texmfdir}/doc/man/man1/dvilj4l.man1.pdf
%doc %{_mandir}/man1/dvilj6.1*
%doc %{_texmfdir}/doc/man/man1/dvilj6.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

# revision 33736
# category TLCore
# catalog-ctan /dviware/dviljk
# catalog-date 2012-04-21 09:41:15 +0200
# catalog-license gpl
# catalog-version 2.6p4
Name:		texlive-dviljk
Version:	2.6p4
Release:	14
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

%description
A dvi driver for the LaserJet printers, using kpathsea
recursive file searching. Note: this program will not compile
simply with the sources in this distribution; it needs a full
(current) kpathsea distribution environment, such as is
available from the TeX-Live source tree.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvihp.1*
%doc %{_texmfdistdir}/doc/man/man1/dvihp.man1.pdf
%doc %{_mandir}/man1/dvilj.1*
%doc %{_texmfdistdir}/doc/man/man1/dvilj.man1.pdf
%doc %{_mandir}/man1/dvilj2p.1*
%doc %{_texmfdistdir}/doc/man/man1/dvilj2p.man1.pdf
%doc %{_mandir}/man1/dvilj4.1*
%doc %{_texmfdistdir}/doc/man/man1/dvilj4.man1.pdf
%doc %{_mandir}/man1/dvilj4l.1*
%doc %{_texmfdistdir}/doc/man/man1/dvilj4l.man1.pdf
%doc %{_mandir}/man1/dvilj6.1*
%doc %{_texmfdistdir}/doc/man/man1/dvilj6.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

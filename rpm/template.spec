%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rqt-bag-plugins
Version:        1.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_bag_plugins package

License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-cairo
Requires:       python3-pillow
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-rclpy
Requires:       ros-iron-rosbag2
Requires:       ros-iron-rqt-bag
Requires:       ros-iron-rqt-gui
Requires:       ros-iron-rqt-gui-py
Requires:       ros-iron-sensor-msgs
Requires:       ros-iron-std-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag files.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Fri Sep 08 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.4-1
- Autogenerated by Bloom

* Fri Jul 14 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.3-1
- Autogenerated by Bloom

* Thu May 11 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.2-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.1-2
- Autogenerated by Bloom

* Tue Apr 11 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.1-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.0-2
- Autogenerated by Bloom


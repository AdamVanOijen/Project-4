#!/usr/bin/env python

"""models.py

Udacity conference server-side Python App Engine data & ProtoRPC models

$Id: models.py,v 1.1 2014/05/24 22:01:10 wesc Exp $

created/forked from conferences.py by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import httplib
import endpoints
from protorpc import messages
from protorpc import message_types
from google.appengine.ext import ndb

class ConflictException(endpoints.ServiceException):
    """ConflictException -- exception mapped to HTTP 409 response"""
    http_status = httplib.CONFLICT

class Profile(ndb.Model):
    """Profile -- User profile object"""
    displayName = ndb.StringProperty()
    mainEmail = ndb.StringProperty()
    teeShirtSize = ndb.StringProperty(default='NOT_SPECIFIED')
    conferenceKeysToAttend = ndb.StringProperty(repeated=True)
    sessionKeysWishlist = ndb.StringProperty(repeated=True)

class ProfileMiniForm(messages.Message):
    """ProfileMiniForm -- update Profile form message"""
    displayName = messages.StringField(1)
    teeShirtSize = messages.EnumField('TeeShirtSize', 2)

class ProfileForm(messages.Message):
    """ProfileForm -- Profile outbound form message"""
    displayName = messages.StringField(1)
    mainEmail = messages.StringField(2)
    teeShirtSize = messages.EnumField('TeeShirtSize', 3)
    conferenceKeysToAttend = messages.StringField(4, repeated=False)

class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    data = messages.StringField(1, required=True)

class BooleanMessage(messages.Message):
    """BooleanMessage-- outbound Boolean value message"""
    data = messages.BooleanField(1)

class Conference(ndb.Model):
    """Conference -- Conference object"""
    name            = ndb.StringProperty(required=True)
    description     = ndb.StringProperty(indexed=False)
    organizerUserId = ndb.StringProperty()
    topics          = ndb.StringProperty(repeated=True)
    city            = ndb.StringProperty()
    startDate       = ndb.DateProperty()
    month           = ndb.IntegerProperty()
    endDate         = ndb.DateProperty()
    maxAttendees    = ndb.IntegerProperty()
    seatsAvailable  = ndb.IntegerProperty()

class SpeakerNameForm(messages.Message):
    """Inbound form containing a speaker's name"""
    name            = messages.StringField(1, required=True)

class FeaturedSpeakerForm(messages.Message):
    """outbound Form containing fields for Speaker name 
    and corresponding Session names"""
    name            = messages.StringField(1)
    sessions        = messages.StringField(2, repeated=True)

class Session(ndb.Model):
    """Session -- Session object"""
    name            = ndb.StringProperty(required=True)
    startTime       = ndb.TimeProperty(required=True)
    speaker         = ndb.StringProperty(required=True)
    duration        = ndb.FloatProperty(indexed=False)
    typeOfSession   = ndb.StringProperty(required=True)
    date            = ndb.DateProperty(required=True)
    highlights      = ndb.StringProperty(indexed=False)
class SessionForm(messages.Message):
    """ SessionForm -- Session outbound/inbound form message"""
    name            = messages.StringField(1)
    startTime       = messages.StringField(2, required=True)
    speaker         = messages.StringField(3, required=True)
    duration        = messages.FloatField(4)#in hours
    typeOfSession   = messages.StringField(5, required=True)
    date            = messages.StringField(6, required=True)
    highlights      = messages.StringField(7)
    websafeKey      = messages.StringField(8)

class SessionForms(messages.Message):
    """Multiple outbound SessionForm messages """
    sessions = messages.MessageField(SessionForm, 1, repeated = True)

class ConferenceForm(messages.Message):
    """ConferenceForm -- Conference outbound form message"""
    name            = messages.StringField(1)
    description     = messages.StringField(2)
    organizerUserId = messages.StringField(3)
    topics          = messages.StringField(4, repeated=True)
    city            = messages.StringField(5)
    startDate       = messages.StringField(6) #DateTimeField()
    month           = messages.IntegerField(7, variant=messages.Variant.INT32)
    maxAttendees    = messages.IntegerField(8, variant=messages.Variant.INT32)
    seatsAvailable  = messages.IntegerField(9, variant=messages.Variant.INT32)
    endDate         = messages.StringField(10) #DateTimeField()
    websafeKey      = messages.StringField(11)
    organizerDisplayName = messages.StringField(12)

class ConferenceForms(messages.Message):
    """ConferenceForms -- multiple Conference outbound form message"""
    items = messages.MessageField(ConferenceForm, 1, repeated=True)

class TeeShirtSize(messages.Enum):
    """TeeShirtSize -- t-shirt size enumeration value"""
    NOT_SPECIFIED = 1
    XS_M = 2
    XS_W = 3
    S_M = 4
    S_W = 5
    M_M = 6
    M_W = 7
    L_M = 8
    L_W = 9
    XL_M = 10
    XL_W = 11
    XXL_M = 12
    XXL_W = 13
    XXXL_M = 14
    XXXL_W = 15

class ConferenceQueryForm(messages.Message):
    """ConferenceQueryForm -- Conference query inbound form message"""
    field = messages.StringField(1)
    operator = messages.StringField(2)
    value = messages.StringField(3)

class ConferenceQueryForms(messages.Message):
    """ConferenceQueryForms -- multiple ConferenceQueryForm inbound form message"""
    filters = messages.MessageField(ConferenceQueryForm, 1, repeated=True)

class SessionQueryForm(messages.Message):
    """Inbound form containing a value corresponding to typeOfSession property of 
    Session Object"""
    typeOfSession = messages.StringField(1, required=True)

class SessionTimeQueryForm(messages.Message):
    """inbound form specifying a segment of time in a day, defined by a max time and a 
    minimum time """
    maxTime       = messages.StringField(1)
    minTime       = messages.StringField(2)

class SessionDateQueryForm(messages.Message):
    """Inbound form containing a segment of time, defined by a max date and a 
    minimum date"""
    maxDate       = messages.StringField(1)
    minDate       = messages.StringField(2)